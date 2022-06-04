import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]},
                  index=['Alice', 'Bob'])

print(df)
#        age state  point
# Alice   24    NY     64
# Bob     42    CA     92

for column_name in df:
    print(column_name)
# age
# state
# point

for column_name, item in df.iteritems():
    print(column_name)
    print('------')
    print(type(item))
    print(item)
    print('------')
    print(item[0], item['Alice'], item.Alice)
    print(item[1], item['Bob'], item.Bob)
    print('======\n')
# age
# ------
# <class 'pandas.core.series.Series'>
# Alice    24
# Bob      42
# Name: age, dtype: int64
# ------
# 24 24 24
# 42 42 42
# ======
# 
# state
# ------
# <class 'pandas.core.series.Series'>
# Alice    NY
# Bob      CA
# Name: state, dtype: object
# ------
# NY NY NY
# CA CA CA
# ======
# 
# point
# ------
# <class 'pandas.core.series.Series'>
# Alice    64
# Bob      92
# Name: point, dtype: int64
# ------
# 64 64 64
# 92 92 92
# ======
# 

for index, row in df.iterrows():
    print(index)
    print('------')
    print(type(row))
    print(row)
    print('------')
    print(row[0], row['age'], row.age)
    print(row[1], row['state'], row.state)
    print(row[2], row['point'], row.point)
    print('======\n')
# Alice
# ------
# <class 'pandas.core.series.Series'>
# age      24
# state    NY
# point    64
# Name: Alice, dtype: object
# ------
# 24 24 24
# NY NY NY
# 64 64 64
# ======
# 
# Bob
# ------
# <class 'pandas.core.series.Series'>
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object
# ------
# 42 42 42
# CA CA CA
# 92 92 92
# ======
# 

for row in df.itertuples():
    print(type(row))
    print(row)
    print('------')
    print(row[0], row.Index)
    print(row[1], row.age)
    print(row[2], row.state)
    print(row[3], row.point)
    print('======\n')
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Alice', age=24, state='NY', point=64)
# ------
# Alice Alice
# 24 24
# NY NY
# 64 64
# ======
# 
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Bob', age=42, state='CA', point=92)
# ------
# Bob Bob
# 42 42
# CA CA
# 92 92
# ======
# 

for row in df.itertuples(name=None):
    print(type(row))
    print(row)
    print(row[0], row[1], row[2], row[3])
    print('======\n')
# <class 'tuple'>
# ('Alice', 24, 'NY', 64)
# Alice 24 NY 64
# ======
# 
# <class 'tuple'>
# ('Bob', 42, 'CA', 92)
# Bob 42 CA 92
# ======
# 

print(df['age'])
# Alice    24
# Bob      42
# Name: age, dtype: int64

print(type(df['age']))
# <class 'pandas.core.series.Series'>

for age in df['age']:
    print(age)
# 24
# 42

for age, point in zip(df['age'], df['point']):
    print(age, point)
# 24 64
# 42 92

print(df.index)
# Index(['Alice', 'Bob'], dtype='object')

print(type(df.index))
# <class 'pandas.core.indexes.base.Index'>

for index in df.index:
    print(index)
# Alice
# Bob

for index, state in zip(df.index, df['state']):
    print(index, state)
# Alice NY
# Bob CA

for index, row in df.iterrows():
    row['point'] += row['age']

print(df)
#        age state  point
# Alice   24    NY     64
# Bob     42    CA     92

for index, row in df.iterrows():
    df.at[index, 'point'] += row['age']

print(df)
#        age state  point
# Alice   24    NY     88
# Bob     42    CA    134

df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]},
                  index=['Alice', 'Bob'])
df['point'] += df['age']
print(df)
#        age state  point
# Alice   24    NY     88
# Bob     42    CA    134

df['new'] = df['point'] + df['age'] * 2
print(df)
#        age state  point  new
# Alice   24    NY     88  136
# Bob     42    CA    134  218

df['age_sqrt'] = np.sqrt(df['age'])
print(df)
#        age state  point  new  age_sqrt
# Alice   24    NY     88  136  4.898979
# Bob     42    CA    134  218  6.480741

df['state_0'] = df['state'].str.lower().str[0]
print(df)
#        age state  point  new  age_sqrt state_0
# Alice   24    NY     88  136  4.898979       n
# Bob     42    CA    134  218  6.480741       c
