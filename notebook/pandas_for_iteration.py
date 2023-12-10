import pandas as pd

print(pd.__version__)
# 2.1.4

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

for column_name, item in df.items():
    print(column_name)
    print(type(item))
    print(item['Alice'], item['Bob'])
    print('======')
# age
# <class 'pandas.core.series.Series'>
# 24 42
# ======
# state
# <class 'pandas.core.series.Series'>
# NY CA
# ======
# point
# <class 'pandas.core.series.Series'>
# 64 92
# ======

for index, row in df.iterrows():
    print(index)
    print(type(row))
    print(row['age'], row['state'], row['point'])
    print('======')
# Alice
# <class 'pandas.core.series.Series'>
# 24 NY 64
# ======
# Bob
# <class 'pandas.core.series.Series'>
# 42 CA 92
# ======

for row in df.itertuples():
    print(type(row))
    print(row)
    print(row[0], row[1], row[2], row[3])
    print(row.Index, row.age, row.state, row.point)
    print('======')
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Alice', age=24, state='NY', point=64)
# Alice 24 NY 64
# Alice 24 NY 64
# ======
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Bob', age=42, state='CA', point=92)
# Bob 42 CA 92
# Bob 42 CA 92
# ======

for row in df.itertuples(index=False, name='Person'):
    print(type(row))
    print(row)
    print(row[0], row[1], row[2])
    print(row.age, row.state, row.point)
    print('======')
# <class 'pandas.core.frame.Person'>
# Person(age=24, state='NY', point=64)
# 24 NY 64
# 24 NY 64
# ======
# <class 'pandas.core.frame.Person'>
# Person(age=42, state='CA', point=92)
# 42 CA 92
# 42 CA 92
# ======

for row in df.itertuples(name=None):
    print(type(row))
    print(row)
    print(row[0], row[1], row[2], row[3])
    print('======')
# <class 'tuple'>
# ('Alice', 24, 'NY', 64)
# Alice 24 NY 64
# ======
# <class 'tuple'>
# ('Bob', 42, 'CA', 92)
# Bob 42 CA 92
# ======

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
print(df)
#        age state  point
# Alice   24    NY     64
# Bob     42    CA     92

df['point'] += df['age']
print(df)
#        age state  point
# Alice   24    NY     88
# Bob     42    CA    134

df['new'] = df['point'] + df['age'] * 2 + 1000
print(df)
#        age state  point   new
# Alice   24    NY     88  1136
# Bob     42    CA    134  1218

import numpy as np

df['age_sqrt'] = np.sqrt(df['age'])
print(df)
#        age state  point   new  age_sqrt
# Alice   24    NY     88  1136  4.898979
# Bob     42    CA    134  1218  6.480741

df['state_0'] = df['state'].str.lower().str[0]
print(df)
#        age state  point   new  age_sqrt state_0
# Alice   24    NY     88  1136  4.898979       n
# Bob     42    CA    134  1218  6.480741       c

df['point_hex'] = df['point'].map(hex)
print(df)
#        age state  point   new  age_sqrt state_0 point_hex
# Alice   24    NY     88  1136  4.898979       n      0x58
# Bob     42    CA    134  1218  6.480741       c      0x86
