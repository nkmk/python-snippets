import pandas as pd

print(pd.__version__)
# 1.4.1

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

l_bool = [True, False, False, True, True, False]
print(df[l_bool])
#        age state  point
# name                   
# Alice   24    NY     64
# Dave    68    TX     70
# Ellen   24    CA     88

# print(df[[True, False, False]])
# ValueError: Item wrong length 3 instead of 6.

s_bool = pd.Series(l_bool, index=reversed(df.index))
print(s_bool)
# Frank       True
# Ellen      False
# Dave       False
# Charlie     True
# Bob         True
# Alice      False
# dtype: bool

print(df[s_bool])
#          age state  point
# name                     
# Bob       42    CA     92
# Charlie   18    CA     70
# Frank     30    NY     57
# 
# <ipython-input-7-6f680b648cc0>:1: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
#   print(df[s_bool])

s_bool_wrong = pd.Series(l_bool, index=['A', 'B', 'C', 'D', 'E', 'F'])

# print(df[s_bool_wrong])
# IndexingError: Unalignable boolean Series provided as indexer
# (index of the boolean Series and of the indexed object do not match).

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

l_bool = [True, False, False, True, True, False]
print(s[l_bool])
# name
# Alice    24
# Dave     68
# Ellen    24
# Name: age, dtype: int64

# print(s[[True, False, False]])
# IndexError: Boolean index has wrong length: 3 instead of 6

s_bool = pd.Series(l_bool, index=reversed(df.index))
print(s_bool)
# Frank       True
# Ellen      False
# Dave       False
# Charlie     True
# Bob         True
# Alice      False
# dtype: bool

print(s[s_bool])
# name
# Bob        42
# Charlie    18
# Frank      30
# Name: age, dtype: int64

s_bool_wrong = pd.Series(l_bool, index=['A', 'B', 'C', 'D', 'E', 'F'])

# print(s[s_bool_wrong])
# IndexingError: Unalignable boolean Series provided as indexer
# (index of the boolean Series and of the indexed object do not match).
