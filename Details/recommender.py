# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load movies dataset
movies = pd.read_csv('dataset/movies.csv')

# Fill NaN genres
movies['genres'] = movies['genres'].fillna('')

# TF-IDF Vectorization on genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Movie title to index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def recommend(title, num=5):
    idx = indices.get(title)
    if idx is None:
        return f"Movie '{title}' not found in the dataset."
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices]

# Example use
movie_name = input("Enter a movie you like: ")
recommendations = recommend(movie_name)
print("\nRecommended Movies:")
print(recommendations)
