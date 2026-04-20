"""import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("Series:\n", s)

# Create with custom index
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Access values and index
print("Values:", s.values)
print("Index:", s.index)



import pandas as pd

# Create DataFrame from dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'London', 'Paris']
}

df = pd.DataFrame(data)

# Inspect data
print("Shape:", df.shape)
print("First 2 rows:\n", df.head(2))


import pandas as pd

# Read data from a CSV file
df_csv = pd.read_csv('data.csv')

# Read data from Excel, specify sheet
df_excel = pd.read_excel('./data.xlsx', sheet_name='Sheet1')

# Read CSV with index column set
df_index = pd.read_csv('data.csv', index_col=0)

# Read CSV selecting specific columns
df_cols = pd.read_csv('data.csv', usecols=['Name', 'Age'])

print(df_index)
print(df_cols)


import pandas as pd

df = pd.read_csv('data.csv')

# View first 5 rows
print("First 5 rows:\n", df.head())

# View concise summary
print("\nData Info:")
print(df.info())

# Get descriptive stats
print("\nStats:\n", df.describe())


import pandas as pd

df = pd.read_csv('data.csv', index_col='Name')

# Select a single column (Series)
ages = df['Age']        # Bracket notation
ages = df.Age           # Dot notation

# Select multiple columns (DataFrame)
subset = df[['Age', 'City']]

# Select rows by label using .loc[]
alice_data = df.loc['Alice']
print('alice_data:\n', alice_data, '\n')

# Select rows by position using .iloc[]
first_row = df.iloc[0]
top_two = df.iloc[0:2]

print('first_row:\n', first_row)
print('top_two:\n', top_two)


import pandas as pd

df = pd.read_csv('data.csv')

# 1. Single condition: Age > 26
adults = df[df['Age'] > 26]
print('adults:', adults, '\n')

# 2. Multiple conditions: Age > 30 AND City == 'Paris'
paris_adults = df[(df['Age'] > 30) & (df['City'] == 'Paris')]
print('paris_adults:', paris_adults, '\n')

# 3. OR condition: Age < 25 OR City == 'NY'
youth_ny = df[(df['Age'] < 25) | (df['City'] == 'NY')]
print('youth_ny:', youth_ny, '\n')




import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan]})
print(df)

# Check for missing values
print(df.isnull())

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Fill missing values with mean
df_filled = df.fillna(df.mean())
print(df_filled)

import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
print(df)

# Add a new column
df['Birth_Year'] = 2024 - df['Age']
print(df)

# Modify an existing column
df['Age'] = df['Age'] + 1
print(df)

# Apply a custom function
def age_group(age):
    if age < 30:
        return 'Young'
    else:
        return 'Senior'

df['Age_Group'] = df['Age'].apply(age_group)

# Map values using a dictionary
city_map = {'Alice': 'NY', 'Bob': 'London'}
df['City'] = df['Name'].map(city_map)


import pandas as pd

df = pd.DataFrame({
    'City': ['Paris', 'London', 'Paris'],
    'Sales': [100, 200, 300]
})
print(df)

# Group by City and calculate sum
city_sales = df.groupby('City')['Sales'].sum()
print(city_sales)

# Multiple aggregations
stats = df.groupby('City')['Sales'].agg(['sum', 'mean'])
print(stats)
"""
import pandas as pd

df = pd.DataFrame({
    'City': ['NY', 'LON', 'PAR'],
    'Product': ['A', 'B', 'A'],
    'Sales': [100, 200, 150]
})
print(df, '\n')

# Create pivot table
pt = pd.pivot_table(
    df, index='City',
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
print(pt)