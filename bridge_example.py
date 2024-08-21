import pandas as pd
import numpy as np

def clean_dataset(df):
    # Remove leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Convert all numeric columns to appropriate type
    numeric_columns = ['Span', 'Width', 'Height']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Format 'Material' column to capitalize all words
    df['Material'] = df['Material'].str.title()

    # Strip whitespace from string columns
    string_columns = ['Bridge Name', 'Material']
    df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())

    # Remove rows with missing values
    df.dropna(inplace=True)

    return df

# Create synthetic data
data = {
    'Bridge Name': ['Golden Gate ', ' Brooklyn', ' London', ' Sydney Harbor', 'Forth '],
    'Span': [1280, 1595, 283, 503, 521],
    'Width': [27, 26, 32, 49, 37],
    'Height': ['227', '84', '13', '134', '110'],
    'Material': ['Steel', 'steel', 'concrete', 'STEEL', 'steel']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean the dataset
cleaned_data = clean_dataset(df)

# Print the cleaned data
print(cleaned_data)