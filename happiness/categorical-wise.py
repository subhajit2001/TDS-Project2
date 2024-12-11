
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with latin-1 encoding
data = pd.read_csv('happiness.csv', encoding='latin-1')

# Display the first few rows of the dataset
print(data.head())

# Select categorical columns 
# In the provided dataset, we have Country name as the primary categorical column.
categorical_columns = ['Country name']
data_selected = data[categorical_columns]

# Display missing values in categorical columns
missing_values = data_selected.isnull().sum()
print("Missing values in categorical columns:")
print(missing_values)

# Handling missing values (You can choose to drop or fill missing values)
# Here we will drop rows with missing values
data_selected = data_selected.dropna()

# Analyze and visualize the categorical column: Count of countries
# Count the number of occurrences for each unique value in 'Country name'
country_counts = data_selected['Country name'].value_counts()

# Plot the counts of countries
plt.figure(figsize=(10, 6))
sns.barplot(y=country_counts.index, x=country_counts.values, palette='viridis')
plt.title('Number of Instances per Country')
plt.xlabel('Count')
plt.ylabel('Country Name')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('country_counts.png')
plt.close()

# Additional analysis can be done based on the analysis requirements.
# For instance, if there's more categorical data in the dataset, add those to the analysis.

print("Analysis complete. Plots saved as .png files.")
