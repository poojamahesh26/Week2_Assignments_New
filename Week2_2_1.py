#⁠From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# 1. Filter 'Manufacturer', 'Model', and 'Type' for every 20th row starting from the first row (row 0)
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

# Display the filtered DataFrame
print(filtered_df)