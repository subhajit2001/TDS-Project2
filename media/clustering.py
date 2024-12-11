
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Load the dataset with latin-1 encoding
df = pd.read_csv('media.csv', encoding='latin-1')

# Step 2: Inspect the dataset
print(df.head())
print(df.info())

# Step 3: Handle missing values
# Let's assume we drop rows with missing values for simplicity
df_cleaned = df.dropna()

# Step 4: Select features for clustering
# We'll use 'overall', 'quality', and 'repeatability' for this example.
features = df_cleaned[['overall', 'quality', 'repeatability']]

# Step 5: Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 6: Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Choose 3 clusters
df_cleaned['cluster'] = kmeans.fit_predict(features_scaled)

# Step 7: Visualize the clusters
# Using PCA to reduce the dimensions for visualization
pca = PCA(n_components=2)
features_pca = pca.fit_transform(features_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=features_pca[:, 0], y=features_pca[:, 1], hue=df_cleaned['cluster'], palette='viridis')
plt.title('KMeans Clustering of Media Dataset')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Clusters')
plt.savefig('kmeans_clustering.png')  # Save the figure
plt.show()

# Step 8: Save the modified dataframe to a new CSV file if needed
df_cleaned.to_csv('media_with_clusters.csv', index=False)
