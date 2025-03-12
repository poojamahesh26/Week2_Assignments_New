#⁠ ⁠Replace missing values in Min.Price and Max.Price columns with their respective mean.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Replace missing values in 'Min.Price' and 'Max.Price' with their respective mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

# Display the updated DataFrame
print(df[['Min.Price', 'Max.Price']].head()) 