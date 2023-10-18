import pandas as pd
import numpy as np

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

# Load the data into a pandas dataframe
df = pd.read_csv('housing.csv', dtype=dtype_dict)

df.dropna(axis=0, inplace=True)

df.fillna(method='ffill', inplace=True)

df.drop_duplicates(inplace=True)

df.to_csv('housing_cleaned.csv', index=False)
