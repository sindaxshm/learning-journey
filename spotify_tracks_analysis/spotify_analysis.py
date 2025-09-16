
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


print("Loading datasets...")

songs_df = pd.read_csv('genres.csv')  
playlists_df = pd.read_csv('playlists.csv')  

# --- EXPLORE BOTH DATASETS ---
print("=== DATA EXPLORATION ===")
print("Main Songs File Shape:", songs_df.shape)
print("Playlists Mapping File Shape:", playlists_df.shape)

print("\nMain Songs File Columns:")
print(songs_df.columns.tolist())
print("\nPlaylists Mapping File Columns:")
print(playlists_df.columns.tolist())

print("\nFirst 3 rows of Main Songs File:")
print(songs_df[['song_name', 'genre', 'danceability', 'energy']].head(3))

print("\nFirst 5 rows of Playlists Mapping File:")
print(playlists_df.head())

# --- DATA CLEANING ---
print("\n=== DATA CLEANING ===")

# Clean the main songs dataset
print("Missing values in main dataset:")
print(songs_df.isnull().sum())

# Drop unnecessary columns
columns_to_drop = ['Unnamed: 0', 'title', 'type', 'id', 'uri', 'track_href', 'analysis_url']
songs_clean = songs_df.drop(columns=columns_to_drop, errors='ignore')

# Drop rows with missing song names
songs_clean = songs_clean.dropna(subset=['song_name'])
print(f"Shape after cleaning: {songs_clean.shape}")

# Check for duplicates
duplicates = songs_clean.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
if duplicates > 0:
    songs_clean = songs_clean.drop_duplicates()
    print(f"Shape after removing duplicates: {songs_clean.shape}")

# --- ANALYSIS ---
print("\n=== ANALYSIS ===")


print("\n1. Top 10 Most Common Genres:")
top_10_genres = songs_clean['genre'].value_counts().head(10)
print(top_10_genres)

print("\n2. Top 5 Genres by Danceability:")
genre_danceability = songs_clean.groupby('genre')['danceability'].mean()
top_dance_genres = genre_danceability.nlargest(5)
for genre, score in top_dance_genres.items():
    print(f"  - {genre}: {score:.3f}")


print("\n3. Top 5 Genres by Energy:")
genre_energy = songs_clean.groupby('genre')['energy'].mean()
top_energy_genres = genre_energy.nlargest(5)
for genre, score in top_energy_genres.items():
    print(f"  - {genre}: {score:.3f}")


print("\n4. Key Correlations:")
corr_dance_energy = songs_clean['danceability'].corr(songs_clean['energy'])
corr_energy_valence = songs_clean['energy'].corr(songs_clean['valence'])
print(f"  - Danceability vs Energy: {corr_dance_energy:.2f}")
print(f"  - Energy vs Valence: {corr_energy_valence:.2f}")

# --- VISUALIZATIONS ---
print("\nCreating visualizations...")
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Visualization 1: Top Genres
plt.figure(figsize=(12, 6))
top_10_genres.plot(kind='bar', color='lightcoral')
plt.title('Top 10 Most Common Music Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_10_genres.png')
plt.show()

# Visualization 2: Danceability by Genre (Top 5 genres)
plt.figure(figsize=(12, 6))
top_5_genres = top_10_genres.head(5).index
top_genres_data = songs_clean[songs_clean['genre'].isin(top_5_genres)]
sns.boxplot(x='genre', y='danceability', data=top_genres_data)
plt.title('Danceability Distribution Across Top 5 Genres')
plt.xlabel('Genre')
plt.ylabel('Danceability')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('danceability_by_genre.png')
plt.show()

# Visualization 3: Energy vs. Valence Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='energy', y='valence', data=songs_clean, alpha=0.3, hue='genre', legend=False)
plt.title('Energy vs. Valence (Colored by Genre)')
plt.xlabel('Energy')
plt.ylabel('Valence (Positivity)')
plt.tight_layout()
plt.savefig('energy_vs_valence.png')
plt.show()

# Visualization 4: Correlation Heatmap
plt.figure(figsize=(10, 8))
audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 
                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
corr_matrix = songs_clean[audio_features].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, square=True)
plt.title('Correlation Heatmap of Audio Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# Visualization 5: Duration Distribution by Genre
plt.figure(figsize=(12, 6))
songs_clean['duration_min'] = songs_clean['duration_ms'] / 60000  # Convert to minutes
top_genres_data = songs_clean[songs_clean['genre'].isin(top_5_genres)]
sns.boxplot(x='genre', y='duration_min', data=top_genres_data)
plt.title('Song Duration Distribution Across Top 5 Genres')
plt.xlabel('Genre')
plt.ylabel('Duration (minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('duration_by_genre.png')
plt.show()