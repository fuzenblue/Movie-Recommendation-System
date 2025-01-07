import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies['genre'] = movies['genre'].apply(lambda x: x if isinstance(x, list) else [])

def recommend(movie, top_n=5):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:top_n + 1]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


def recommend_by_genres(genres, top_n=5):
    filtered_data = movies[movies['genre'].apply(lambda x: all(g in x for g in genres))]
    if not filtered_data.empty:
        top_movies = filtered_data.head(top_n)
        recommend_movie = top_movies['title'].tolist()
        recommend_poster = [fetch_poster(movies.loc[i, 'id']) for i in top_movies.index]
        return recommend_movie, recommend_poster
    else:
        return [], []


def recommend_by_genres_and_title(movie, genres, top_n=5):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    movie_based_recommendations = [movies.iloc[i[0]].title for i in distance[1:len(movies)]]

    filtered_movies = movies[movies['genre'].apply(lambda x: any(genre in x for genre in genres))]
    
    if not filtered_movies.empty:
        genre_counts = {}
        for movie_title in movie_based_recommendations:
            if movie_title in filtered_movies['title'].values:
                movie_row = filtered_movies[filtered_movies['title'] == movie_title]
                genres_in_movie = movie_row.iloc[0]['genre']
                count = sum([1 for g in genres if g in genres_in_movie])
                genre_counts[movie_title] = count

        sorted_movies = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
        result_movies = [movie[0] for movie in sorted_movies[:top_n]]
        result_posters = [fetch_poster(movies[movies['title'] == m].iloc[0].id) for m in result_movies]
        return result_movies, result_posters

    return [], []

st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
    ]

imageCarouselComponent(imageUrls=imageUrls, height=200)


movies_list = movies['title'].values
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

genres = [
    "Drama", "Comedy", "Thriller", "Action", "Romance", "Adventure", "Crime",
    "Horror", "Family", "ScienceFiction", "Fantasy", "Animation", "Mystery",
    "History", "War", "Music", "Western", "TVMovie"
]

selected_genres = st.multiselect("Select Genres", genres)

if st.button("Recommend"):
    if selectvalue and selected_genres:
        st.write("### Recommendations based on Title and Genres")
        movie_name, movie_poster = recommend_by_genres_and_title(selectvalue, selected_genres)
    elif selectvalue:
        st.write("### Recommendations based on Title")
        movie_name, movie_poster = recommend(selectvalue)
    elif selected_genres:
        st.write("### Recommendations based on Genres")
        movie_name, movie_poster = recommend_by_genres(selected_genres)
    else:
        st.write("Please select a movie or genres to get recommendations.")
        movie_name, movie_poster = [], []

    # แสดงผล
    if movie_name:
        col1, col2, col3, col4, col5 = st.columns(5)
        if len(movie_name) >= 1:
            with col1:
                st.text(movie_name[0])
                st.image(movie_poster[0])
        if len(movie_name) >= 2:
            with col2:
                st.text(movie_name[1])
                st.image(movie_poster[1])
        if len(movie_name) >= 3:
            with col3:
                st.text(movie_name[2])
                st.image(movie_poster[2])
        if len(movie_name) >= 4:
            with col4:
                st.text(movie_name[3])
                st.image(movie_poster[3])
        if len(movie_name) >= 5:
            with col5:
                st.text(movie_name[4])
                st.image(movie_poster[4])
    else:
        st.write("No recommendations found.")