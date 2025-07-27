import pandas as pd
import numpy as np

# Load the complete dataset
df = pd.read_csv('EAI.csv')

# Data Cleaning - keep all rows, only remove if Country is completely missing
df = df.dropna(subset=['Country'], how='all')

# Convert numeric columns - fill blanks with 0 and handle commas
numeric_cols = ['Export', 'Import', 'Total Trade', 'Trade Balance']
for col in numeric_cols:
    # Convert to string, replace commas, then to numeric
    df[col] = df[col].astype(str).str.replace(',', '')
    # Convert to numeric, forcing errors to NaN, then fill with 0
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Fill any remaining NaN values with 0 (for non-numeric columns if any)
df = df.fillna(0)

# Create Year column from Financial Year(start) and fill blanks with 0
df['Year'] = df['Financial Year(start)'].astype(str).str.extract('(\d+)')[0].fillna(0).astype(int)

# Add India's perspective columns
df['India_Imports'] = df['Export']  # Other countries' exports to India (India's imports)
df['India_Exports'] = df['Import']  # Other countries' imports from India (India's exports)
df['India_Trade_Balance'] = df['India_Exports'] - df['India_Imports']

# Save the complete dataset with all countries and all years
output_filename = 'Complete_India_Trade_Data_All_Countries_Filled.csv'
df.to_csv(output_filename, index=False)

# Verification
print(f"Total records processed: {len(df)}")
print(f"Total unique countries: {df['Country'].nunique()}")
print(f"Years covered: {df['Year'].min()} to {df['Year'].max()}")

# Display sample data showing blanks are filled with 0
print("\nSample data with blanks filled (first 15 rows):")
print(df.head(15))

# Display alphabetical list of countries
print("\nAlphabetical list of first 20 countries:")
print(sorted(df['Country'].unique())[:20])
