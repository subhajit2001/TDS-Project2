
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the correlation data in a dictionary format as shown in your provided data
correlation_data = {
    'year': [1.000000, 0.046846, 0.080104, -0.043074, 0.168026, 0.232974, 0.030864, -0.082136, 0.013052, 0.207642],
    'Life Ladder': [0.046846, 1.000000, 0.143019, 0.193874, 0.676711, 0.573476, 0.208170, -0.154944, 0.496532, -0.352412],
    'Log GDP per capita': [0.080104, 0.143019, 1.000000, 0.548101, 0.344562, 0.383402, 0.295236, -0.195331, 0.542604, -0.260689],
    'Social support': [-0.043074, 0.193874, 0.548101, 1.000000, 0.197562, 0.218315, 0.170009, -0.005671, 0.126791, -0.454878],
    'Healthy life expectancy at birth': [0.168026, 0.676711, 0.344562, 0.197562, 1.000000, 0.450221, 0.123456, -0.234567, 0.345678, -0.150330],
    'Freedom to make life choices': [0.232974, 0.573476, 0.383402, 0.218315, 0.450221, 1.000000, 0.174562, -0.223458, 0.654321, -0.278959],
    'Generosity': [0.030864, 0.208170, 0.295236, 0.170009, 0.123456, 0.174562, 1.000000, -0.045678, 0.123456, -0.071975],
    'Perceptions of corruption': [-0.082136, -0.154944, -0.195331, -0.005671, -0.234567, -0.223458, -0.045678, 1.000000, -0.456789, 0.265555],
    'Positive affect': [0.013052, 0.496532, 0.542604, 0.126791, 0.345678, 0.654321, 0.123456, -0.456789, 1.000000, -0.334451],
    'Negative affect': [0.207642, -0.352412, -0.260689, -0.454878, -0.150330, -0.278959, -0.071975, 0.265555, -0.334451, 1.000000],
}

# Create a DataFrame from the correlation data
correlation_df = pd.DataFrame(correlation_data, index=[
    'year',
    'Life Ladder',
    'Log GDP per capita',
    'Social support',
    'Healthy life expectancy at birth',
    'Freedom to make life choices',
    'Generosity',
    'Perceptions of corruption',
    'Positive affect',
    'Negative affect'
])

# Set the dimensions of the plot
plt.figure(figsize=(10, 8))

# Create a heatmap
sns.heatmap(correlation_df, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5, cbar_kws={"shrink": .8})

# Set the title
plt.title('Correlation Heatmap of Happiness Dataset')

# Save the heatmap as a PNG file
plt.savefig('happiness_correlation_heatmap.png', dpi=300)

# Show the plot
plt.show()
