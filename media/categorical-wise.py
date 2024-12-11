
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset with latin-1 encoding
df = pd.read_csv('media.csv', encoding='latin-1')

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Selecting only categorical columns for analysis
categorical_cols = ['date', 'language', 'type', 'title', 'by']  # Adjusted according to provided columns

# Handle missing values by filling them with a placeholder or dropping
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# Check for unique values in categorical columns
for col in categorical_cols:
    print(f'Unique values in {col}: {df[col].unique()}')

# Analyze categorical features
for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{col}_distribution.png')
    plt.close()

print("Analysis complete and plots saved as PNG files.")
