import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.index)
# Index(['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'], dtype='object', name='name')

print(df.index.str.contains('li'))
# [ True False  True False False False]

print(df[df.index.str.contains('li')])
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70

print(df.index.str.endswith('e'))
# [ True False  True  True False False]

print(df[df.index.str.endswith('e')])
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70

print(df.columns)
# Index(['age', 'state', 'point'], dtype='object')

print(df.columns.str.endswith('e'))
# [ True  True False]

print(df.loc[:, df.columns.str.endswith('e')])
#          age state
# name              
# Alice     24    NY
# Bob       42    CA
# Charlie   18    CA
# Dave      68    TX
# Ellen     24    CA
# Frank     30    NY

print(df.iloc[:, df.columns.str.endswith('e')])
#          age state
# name              
# Alice     24    NY
# Bob       42    CA
# Charlie   18    CA
# Dave      68    TX
# Ellen     24    CA
# Frank     30    NY

print(df.loc[df.index.str.contains('li'), df.columns.str.endswith('e')])
#          age state
# name              
# Alice     24    NY
# Charlie   18    CA
