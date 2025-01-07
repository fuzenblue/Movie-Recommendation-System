# Movie Recommender System with Genre-Based Filtering and Enhanced User Experience

## Description
A Python-based movie recommender system developed using Streamlit. This project enhances an existing implementation by adding genre-based filtering, mixed title-genre recommendations, and improving the user interface and data processing for better functionality and usability.

## Inspiration and References
This project was inspired by the open-source repository: [https://github.com/Chando0185/movie_recommender_system.git]

## Key Features
- **Genre-Based Recommendations**: 
  - Allows users to filter movies by selecting one or more genres.
  - Supports both flexible ( any genre) and strict ( all genres) matching criteria.
- **Mixed Title-Genre Recommendations**: 
  - Combines movie title similarity with user-selected genres for more tailored suggestions.
- **Enhanced Data Preprocessing**:
  - Standardized and cleaned genre data, filling missing values and splitting into lists.
- **Algorithm Optimization**:
  - Introduced a customizable top_n parameter to adjust the number of recommendations.
  - Improved filtering logic with cosine similarity combined with genre filters.

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Data Processing**: Pandas, Scikit-learn
- **Visualization**: Dynamic poster fetching via The Movie Database (TMDB) API
- **Development Approach**: Iterative improvement and feature expansion

## Results
- Improved recommendation accuracy and user satisfaction with personalized suggestions.
- Reduced inconsistencies in data processing, resulting in cleaner outputs.
- Enhanced user interaction through a visually appealing and intuitive UI.
