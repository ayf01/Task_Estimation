import pandas as pd

# Load both CSV files
df1 = pd.read_csv('Dataset_1.csv')
df2 = pd.read_csv('Dataset_2.csv')

# Concatenate the dataframes
combined_df = pd.concat([df1, df2])

# Optionally reset the index if you want a clean index column
combined_df.reset_index(drop=True, inplace=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('Dataset.csv', index=False)
