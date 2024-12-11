
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
file_path = 'goodreads.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Display initial data info
print(data.info())

# Handling missing values
# You might want to investigate how to fill or drop missing values depending on the feature context
# For illustration, let's drop rows with missing values in the 'average_rating' and 'ratings_count'
data = data.dropna(subset=['average_rating', 'ratings_count'])

# Selecting features for clustering
features = ['average_rating', 'ratings_count', 'work_ratings_count', 'work_text_reviews_count']
X = data[features]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine number of clusters using the Elbow Method
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)

# Plot the Elbow Method Graph
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('SSE')
plt.grid()
plt.savefig('elbow_method.png')
plt.close()

# From the elbow plot, you can choose an optimal number of clusters, for example 3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
data['cluster'] = kmeans.fit_predict(X_scaled)

# Reduce dimensions for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a DataFrame for PCA results
pca_df = pd.DataFrame(data={'PC1': X_pca[:, 0], 'PC2': X_pca[:, 1], 'Cluster': data['cluster']})

# Plotting the clustered results
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_df, palette='Set1', s=100)
plt.title('PCA of Clusters')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid()
plt.savefig('cluster_visualization.png')
plt.close()

print("Clustering analysis completed. Plots saved as 'elbow_method.png' and 'cluster_visualization.png'.")
