import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    # Using your actual API key
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0b2b523bdb6fde5e8232d1cf88f344f1&language=en-US".format(
        movie_id)
    try:
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:

            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"Error fetching poster: {e}")


    return "https://via.placeholder.com/500x750?text=Poster+Not+Found"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]


    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        # CRITICAL: Make sure 'movie_id' matches the column name in your pickle file
        tmdb_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster using TMDB ID
        recommended_movies_posters.append(fetch_poster(tmdb_id))

    return recommended_movies, recommended_movies_posters


# --- Load Data ---
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Pickle files not found! Ensure 'movie_dict.pkl' and 'similarity.pkl' are in the same folder.")

# --- Streamlit UI ---
st.set_page_config(layout="wide")
st.title('Movies Recommendation System')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values if 'movies' in locals() else []
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Creating 5 columns for the 5 recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])