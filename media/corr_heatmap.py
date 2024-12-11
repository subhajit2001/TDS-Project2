
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame with the correlation data
correlation_data = {
    'overall': [1.000000, 0.825935, 0.512600],
    'quality': [0.825935, 1.000000, 0.312127],
    'repeatability': [0.512600, 0.312127, 1.000000]
}
columns = ['overall', 'quality', 'repeatability']

correlation_df = pd.DataFrame(correlation_data, index=columns)

# Set the size of the plot
plt.figure(figsize=(8, 6))

# Create a heatmap
sns.heatmap(correlation_df, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, vmin=-1, vmax=1)

# Set the title
plt.title('Correlation Heatmap')

# Save the heatmap as a PNG file
plt.savefig('correlation_heatmap.png', dpi=300)

# Show the plot (optional)
plt.show()
