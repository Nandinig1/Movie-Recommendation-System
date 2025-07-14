import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
movies = pd.read_csv('movies.csv')  # Make sure this file is in the same folder
movies['genres'] = movies['genres'].fillna('')

# Convert genres to vector format
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Create similarity scores
similarity = cosine_similarity(tfidf_matrix)

# Define the recommend function
def recommend(movie_name):
    try:
        movie_index = movies[movies['title'].str.contains(movie_name, case=False)].index[0]
        sim_scores = list(enumerate(similarity[movie_index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
        recommended = [movies.iloc[i[0]]['title'] for i in sim_scores]
        return recommended
    except:
        return ["Movie not found. Try typing something else!"]

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Type a movie you like, and we’ll suggest 5 similar ones!")

user_input = st.text_input("Enter a movie name")

if st.button("Recommend"):
    results = recommend(user_input)
    st.write("### Recommended Movies:")
    for movie in results:
        st.write(f"- {movie}")
