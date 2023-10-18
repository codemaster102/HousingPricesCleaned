import pandas as pd

dtype_dict = {
    'CRIM': 'float64',     # Example: Integer data type
    'ZN': 'float32',   # Example: Floating-point data type
    'INDUS': 'float64',     # Example: Object (string) data type
    'CHAS': 'int32',  
    'NOX': 'float64',  
    'RM': 'float64',
    'AGE': 'float32',  
    'DIS': 'float64', 
    'RAD': 'int32', 
    'TAX': 'float32', 
    'PTRATIO': 'float32',  
    'MEDV': 'float32',  
    'B': 'float32',  
    'LSTAT': 'float32'     
}

# Read the CSV files into Pandas DataFrames
df1 = pd.read_csv('housing.csv', dtype=dtype_dict)
df2 = pd.read_csv('housing_cleaned.csv', dtype=dtype_dict)

# Find rows in df1 that are not in df2
diff_df1 = pd.merge(df1, df2, on=df1.columns.tolist(), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])

# Find rows in df2 that are not in df1
diff_df2 = pd.merge(df1, df2, on=df1.columns.tolist(), how='right', indicator=True).query('_merge == "right_only"').drop(columns=['_merge'])

# Display the differences
print("Differences in df1:")
print(diff_df1)

print("Differences in df2:")
print(diff_df2)

# # Export the differences to CSV files
# diff_df1.to_csv('differences_in_df1.csv', index=False)
# diff_df2.to_csv('differences_in_df2.csv', index=False)
