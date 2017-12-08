import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0).head(2)
print(df)
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92

for column_name in df:
    print(type(column_name))
    print(column_name)
    print('======\n')
# <class 'str'>
# age
# ======
# <class 'str'>
# state
# ======
# <class 'str'>
# point
# ======

for column_name, item in df.iteritems():
    print(type(column_name))
    print(column_name)
    print(type(item))
    print(item)
    print('------')
    
    print(item['Alice'])
    print(item[0])
    print(item.Alice)
    print('======\n')
# <class 'str'>
# age
# <class 'pandas.core.series.Series'>
# name
# Alice    24
# Bob      42
# Name: age, dtype: int64
# ------
# 24
# 24
# 24
# ======
# <class 'str'>
# state
# <class 'pandas.core.series.Series'>
# name
# Alice    NY
# Bob      CA
# Name: state, dtype: object
# ------
# NY
# NY
# NY
# ======
# <class 'str'>
# point
# <class 'pandas.core.series.Series'>
# name
# Alice    64
# Bob      92
# Name: point, dtype: int64
# ------
# 64
# 64
# 64
# ======

for index, row in df.iterrows():
    print(type(index))
    print(index)
    print(type(row))
    print(row)
    print('------')
    
    print(row['point'])
    print(row[2])
    print(row.point)
    print('======\n')
# <class 'str'>
# Alice
# <class 'pandas.core.series.Series'>
# age      24
# state    NY
# point    64
# Name: Alice, dtype: object
# ------
# 64
# 64
# 64
# ======
# <class 'str'>
# Bob
# <class 'pandas.core.series.Series'>
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object
# ------
# 92
# 92
# 92
# ======

for row in df.itertuples():
    print(type(row))
    print(row)
    print('------')
    
    print(row[3])
    print(row.point)
    print('======\n')
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Alice', age=24, state='NY', point=64)
# ------
# 64
# 64
# ======
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Bob', age=42, state='CA', point=92)
# ------
# 92
# 92
# ======

for row in df.itertuples(name=None):
    print(type(row))
    print(row)
    print('------')
    
    print(row[3])
    print('======\n')
# <class 'tuple'>
# ('Alice', 24, 'NY', 64)
# ------
# 64
# ======
# <class 'tuple'>
# ('Bob', 42, 'CA', 92)
# ------
# 92
# ======

for index, row in df.iterrows():
    row.point /= 2

print(df)
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92

for index, row in df.iterrows():
    df.at[index, 'point'] /= 2

print(df)
#        age state  point
# name                   
# Alice   24    NY     32
# Bob     42    CA     46

df['point'] /= 2

print(df)
#        age state  point
# name                   
# Alice   24    NY   16.0
# Bob     42    CA   23.0
