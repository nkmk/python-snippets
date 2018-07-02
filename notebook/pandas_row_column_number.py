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

print(df.index.get_loc('Alice'))
# 0

print(df.index.get_loc('Ellen'))
# 4

print(df.columns.get_loc('age'))
# 0

print(df.columns.get_loc('point'))
# 2

# print(df.index.get_loc('XXX'))
# KeyError: 'XXX'

# print(df.columns.get_loc('XXX'))
# KeyError: 'XXX'

df_dup = df.rename(index={'Charlie': 'Bob'})
print(df_dup)
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92
# Bob     18    CA     70
# Dave    68    TX     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(df_dup.index.get_loc('Bob'))
# slice(1, 3, None)

print(type(df_dup.index.get_loc('Bob')))
# <class 'slice'>

df_dup.rename(index={'Ellen': 'Bob'}, inplace=True)
print(df_dup)
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92
# Bob     18    CA     70
# Dave    68    TX     70
# Bob     24    CA     88
# Frank   30    NY     57

print(df_dup.index.get_loc('Bob'))
# [False  True  True False  True False]

print(type(df_dup.index.get_loc('Bob')))
# <class 'numpy.ndarray'>

print(df_dup[df_dup.index.get_loc('Bob')])
#       age state  point
# name                  
# Bob    42    CA     92
# Bob    18    CA     70
# Bob    24    CA     88

print(df_dup.iloc[df_dup.index.get_loc('Bob'), 0])
# name
# Bob    42
# Bob    18
# Bob    24
# Name: age, dtype: int64

print(df_dup.query('index == "Bob"'))
#       age state  point
# name                  
# Bob    42    CA     92
# Bob    18    CA     70
# Bob    24    CA     88

l_index = list(df.index)
print(l_index)
# ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank']

print(type(l_index))
# <class 'list'>

l_columns = list(df.columns)
print(l_columns)
# ['age', 'state', 'point']

print(type(l_columns))
# <class 'list'>

print(l_index.index('Bob'))
# 1

l_index_dup = list(df_dup.index)
print(l_index_dup)
# ['Alice', 'Bob', 'Bob', 'Dave', 'Bob', 'Frank']

print([i for i, x in enumerate(l_index_dup) if x == 'Bob'])
# [1, 2, 4]

print(df.query('state == "CA"'))
#          age state  point
# name                     
# Bob       42    CA     92
# Charlie   18    CA     70
# Ellen     24    CA     88

print(list(df.query('state == "CA"').index))
# ['Bob', 'Charlie', 'Ellen']

print(df.query('state == "TX"'))
#       age state  point
# name                  
# Dave   68    TX     70

print(list(df.query('state == "TX"').index))
# ['Dave']

print(df.query('state == "TX"').index[0])
# Dave

print(df.reset_index())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(list(df.reset_index().query('state == "CA"').index))
# [1, 2, 4]

print(list(df.reset_index().query('state == "TX"').index))
# [3]

print(df.reset_index().query('state == "TX"').index[0])
# 3
