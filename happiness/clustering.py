
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
file_path = 'happiness.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Display the first few rows of the dataset
print(data.head())

# Selecting relevant features for clustering
features = [
    'Life Ladder', 
    'Log GDP per capita', 
    'Social support', 
    'Healthy life expectancy at birth', 
    'Freedom to make life choices', 
    'Generosity', 
    'Perceptions of corruption'
]
data_features = data[features]

# Handle missing values (for this example, we'll drop them)
data_features = data_features.dropna()

# Standardize the features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_features)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # You can change the number of clusters
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Visualize the clusters using PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Create a DataFrame for plotting
plot_data = pd.DataFrame(data_pca, columns=['PCA1', 'PCA2'])
plot_data['Cluster'] = data['Cluster']

# Plot the clusters
plt.figure(figsize=(10, 8))
sns.scatterplot(data=plot_data, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=100)
plt.title('K-Means Clustering of Happiness Data', fontsize=15)
plt.xlabel('Principal Component 1', fontsize=12)
plt.ylabel('Principal Component 2', fontsize=12)
plt.legend(title='Cluster', fontsize=12)
plt.grid()
plt.savefig('happiness_clustering.png')  # Save the plot as a PNG file
plt.show()
