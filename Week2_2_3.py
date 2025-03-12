import pandas as pd
import numpy as np

# Create the DataFrame with random integers
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# Get rows where the row sum is greater than 100
filtered_rows = df[df.sum(axis=1) > 100]

# Display the filtered DataFrame
print(filtered_rows)