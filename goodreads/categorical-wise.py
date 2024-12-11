
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'goodreads.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Display the first few rows to understand the data structure (optional)
print(data.head())

# Identify categorical columns from the dataset
# Typically, columns such as 'authors', 'language_code', 'original_title', and 'title' are categorical.
categorical_columns = ['authors', 'language_code', 'original_title', 'title']

# Dealing with missing values (optional: you can choose to drop or fill)
# Here, we'll drop rows with missing values in categorical columns
data_cleaned = data[categorical_columns].dropna()

# Perform analysis on each categorical column
for column in categorical_columns:
    plt.figure(figsize=(12, 6))
    
    # Count the frequency of each category in the column
    sns.countplot(data=data_cleaned, y=column, order=data_cleaned[column].value_counts().index)
    
    # Set plot title and labels
    plt.title(f'Count of each category in {column}')
    plt.xlabel('Count')
    plt.ylabel(column)
    
    # Save the plot as .png file
    plt.tight_layout()
    plt.savefig(f'{column}_category_count.png', dpi=300)
    plt.close()

print("Categorical analysis plots saved as PNG files.")
