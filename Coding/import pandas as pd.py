import pandas as pd

# List of dataset filenames
datasets = [
    'dataset1.csv', 'dataset2.csv', 'dataset3.csv',
    'dataset4.csv', 'dataset5.csv', 'dataset6.csv', 'dataset7.csv'
]

# Function to standardize units to Ktoe
def standardize_units(df, column, unit):
    conversion_factors = {
        'TWh': 860,    # 1 TWh = 860 Ktoe
        'Btu': 0.0000252, # 1 Btu = 0.0000252 Ktoe
        'EJ': 23884.6, # 1 EJ = 23884.6 Ktoe
        'PJ': 23.8846, # 1 PJ = 23.8846 Ktoe
        'Ktoe': 1      # 1 Ktoe = 1 Ktoe
    }
    df[column] = df[column] * conversion_factors[unit]
    return df

# Merging datasets
merged_df = pd.DataFrame()

for dataset in datasets:
    df = pd.read_csv(dataset)
    # Standardize units
    df = standardize_units(df, 'energy_consumption', 'TWh') # Change 'TWh' to appropriate unit for each dataset
    # Remove unwanted attributes
    df = df[['relevant_attribute1', 'relevant_attribute2', 'energy_consumption']] # Keep only relevant attributes
    # Handle outliers
    df = df[(df['energy_consumption'] > lower_bound) & (df['energy_consumption'] < upper_bound)] # Define bounds
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save merged and cleaned dataset
merged_df.to_csv('merged_dataset.csv', index=False)
