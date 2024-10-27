import pandas as pd

# Load Excel file into a pandas DataFrame
df = pd.read_csv('../Data/Dataset.csv')

# Create empty lists to store column information
column_names = []
column_types = []
unique_values_list = []

# Iterate through columns and store column name, type, and unique values
for col in df.columns:
    col_name = col
    col_type = df[col].dtype
    unique_values = df[col].unique()
    
    # Append column information to respective lists
    column_names.append(col_name)
    column_types.append(col_type)
    unique_values_list.append(unique_values)

# Create a new DataFrame to store column information
column_info = pd.DataFrame({
    'Column Name': column_names,
    'Column Type': column_types,
    'Unique Values': unique_values_list
})

# Print the column information
print(column_info)

# Save the column information to a new Excel sheet
column_info.to_excel('metadata.xlsx', index=False)
