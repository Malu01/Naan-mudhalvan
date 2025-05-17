# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs('images', exist_ok=True)

# Load data
movies = pd.read_csv('dataset/movies.csv')
ratings = pd.read_csv('dataset/ratings.csv')

# Merge both
data = pd.merge(ratings, movies, on='movieId')

# Top 10 most rated movies
top_rated = data['title'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_rated.values, y=top_rated.index, palette='viridis')
plt.title('Top 10 Most Rated Movies')
plt.xlabel('Number of Ratings')
plt.tight_layout()
plt.savefig('images/top_rated_movies.png')
plt.close()

# Average ratings of top 10 movies
top_avg = data.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_avg.values, y=top_avg.index, palette='magma')
plt.title('Top 10 Highest Rated Movies')
plt.xlabel('Average Rating')
plt.tight_layout()
plt.savefig('images/top_avg_movies.png')
plt.close()
