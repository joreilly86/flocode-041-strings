import pandas as pd

def clean_borehole_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    print("Original column names:")
    print(df.columns.tolist())
    
    # Clean up column names using string methods
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    print("\nCleaned column names:")
    print(df.columns.tolist())
    
    # Clean up soil type using string methods
    df['soil_type'] = df['soil_type'].str.strip().str.title()
    
    # Convert date to datetime
    df['date_sampled'] = pd.to_datetime(df['date_sampled'], format='%d/%m/%Y')
    
    # Replace 'NP' with 'Non-Plastic' for clarity
    df = df.replace('NP', 'Non-Plastic')
    
    return df

# Use the function - be careful with the file path if you are running with a different directory structure
cleaned_df = clean_borehole_data('../data/borehole_data.xlsx')

print("\nCleaned DataFrame (first few rows):")
print(cleaned_df.head().to_string(index=False))

# Optionally, save the cleaned data to a new Excel file
cleaned_df.to_excel('../data/cleaned_borehole_data.xlsx', index=False)
