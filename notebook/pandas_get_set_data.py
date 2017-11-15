import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.index.values)
# [0 1 2 3 4 5]

print(df.columns.values)
# ['name' 'age' 'state' 'point']

print(df.at[1, 'age'])
print(df.at[3, 'state'])
# 42
# TX

df.at[1, 'age'] = 60
print(df.at[1, 'age'])
# 60

print(df.iat[1, 1])
print(df.iat[3, 2])
# 60
# TX

df.iat[1, 1] = 42
print(df.iat[1, 1])
# 42

print(df.loc[1, 'age'])
print(df.iloc[3, 2])
# 42
# TX

df.loc[1, 'age'] = 60
print(df.loc[1, 'age'])
# 60

print(df.loc[1:3, 'age'])
print(type(df.loc[1:3, 'age']))
# 1    60
# 2    18
# 3    68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.loc[1:3, 'age':'point'])
print(type(df.loc[1:3, 'age':'point']))
#    age state  point
# 1   60    CA     92
# 2   18    CA     70
# 3   68    TX     70
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[[1, 3], ['age', 'point']])
print(type(df.loc[1:3, ['age', 'point']]))
#    age  point
# 1   60     92
# 3   68     70
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[2])
print(type(df.iloc[2]))
# name     Charlie
# age           18
# state         CA
# point         70
# Name: 2, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[1:3])
print(type(df.iloc[1:3]))
#       name  age state  point
# 1      Bob   60    CA     92
# 2  Charlie   18    CA     70
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[:, 'state'])
print(type(df.loc[:, 'state']))
# 0    NY
# 1    CA
# 2    CA
# 3    TX
# 4    CA
# 5    NY
# Name: state, dtype: object
# <class 'pandas.core.series.Series'>

df.loc[1:3, 'age'] = [20, 30, 40]
print(df.loc[1:3, 'age'])
# 1    20
# 2    30
# 3    40
# Name: age, dtype: int64

df_name = df.set_index('name')
# df_name = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
print(df_name)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df_name.index.values)
# ['Alice' 'Bob' 'Charlie' 'Dave' 'Ellen' 'Frank']

print(df_name.at['Alice', 'age'])
print(df_name.at['Dave', 'state'])
# 24
# TX

print(df_name.loc['Alice'])
print(type(df_name.loc['Alice']))
# age      24
# state    NY
# point    64
# Name: Alice, dtype: object
# <class 'pandas.core.series.Series'>

print(df_name.loc[['Alice', 'Frank']])
print(type(df_name.loc[['Alice', 'Frank']]))
#        age state  point
# name                   
# Alice   24    NY     64
# Frank   30    NY     57
# <class 'pandas.core.frame.DataFrame'>

df_state = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=2)
print(df_state)
#           name  age  point
# state                     
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

print(df_state.index.values)
# ['NY' 'CA' 'CA' 'TX' 'CA' 'NY']

print(df_state.at['NY', 'age'])
print(type(df_state.at['NY', 'age']))
# [24 30]
# <class 'numpy.ndarray'>

print(df_state.iat[0, 1])
# 24

print(df_state.index.is_unique)
# False

print(df['name'])
print(type(df['name']))
# 0      Alice
# 1        Bob
# 2    Charlie
# 3       Dave
# 4      Ellen
# 5      Frank
# Name: name, dtype: object
# <class 'pandas.core.series.Series'>

print(df[['name', 'point']])
print(type(df[['name', 'point']]))
#       name  point
# 0    Alice     64
# 1      Bob     92
# 2  Charlie     70
# 3     Dave     70
# 4    Ellen     88
# 5    Frank     57
# <class 'pandas.core.frame.DataFrame'>

print(df.name)
print(type(df.name))
# 0      Alice
# 1        Bob
# 2    Charlie
# 3       Dave
# 4      Ellen
# 5      Frank
# Name: name, dtype: object
# <class 'pandas.core.series.Series'>

print(df[1:3])
print(type(df[1:3]))
#       name  age state  point
# 1      Bob   20    CA     92
# 2  Charlie   30    CA     70
# <class 'pandas.core.frame.DataFrame'>

# print(df[1])
# KeyError
print(df[1:2])
print(type(df[1:2]))
#   name  age state  point
# 1  Bob   20    CA     92
# <class 'pandas.core.frame.DataFrame'>
