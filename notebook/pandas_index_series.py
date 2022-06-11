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

s = df['age']
print(s)
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64

print(s[3])
print(type(s[3]))
# 68
# <class 'numpy.int64'>

print(s[-1])
print(type(s[-1]))
# 30
# <class 'numpy.int64'>

print(s['Dave'])
print(type(s['Dave']))
# 68
# <class 'numpy.int64'>

print(s.Dave)
print(type(s.Dave))
# 68
# <class 'numpy.int64'>

print(s[[1, 3]])
print(type(s[[1, 3]]))
# name
# Bob     42
# Dave    68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[['Dave', 'Bob']])
print(type(s[['Dave', 'Bob']]))
# name
# Dave    68
# Bob     42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[[1]])
print(type(s[[1]]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[['Bob']])
print(type(s[['Bob']]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[1:3])
print(type(s[1:3]))
# name
# Bob        42
# Charlie    18
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s['Bob':'Dave'])
print(type(s['Bob':'Dave']))
# name
# Bob        42
# Charlie    18
# Dave       68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s[1:2])
print(type(s[1:2]))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(s['Bob':'Bob'])
print(type(s['Bob':'Bob']))
# name
# Bob    42
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>
