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

print(df.at['Bob', 'age'])
# 42

df.at['Bob', 'age'] = 60
print(df.at['Bob', 'age'])
# 60

print(df.iat[1, 0])
# 60

df.iat[1, 0] = 42
print(df.iat[1, 0])
# 42

print(df.loc['Bob', 'age'])
# 42

print(df.iloc[1, 0])
# 42

df.loc['Bob', 'age'] = 60
print(df.loc['Bob', 'age'])
# 60

df.iloc[1, 0] = 42
print(df.iloc[1, 0])
# 42

print(df.loc['Bob':'Dave', 'age'])
print(type(df.loc['Bob':'Dave', 'age']))
# name
# Bob        42
# Charlie    18
# Dave       68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.loc[:'Dave', ['age', 'point']])
print(type(df.loc[:'Dave', 'age':'point']))
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:3, [0, 2]])
print(type(df.iloc[:3, [0, 2]]))
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[::2, 0])
print(type(df.iloc[::2, 0]))
# name
# Alice      24
# Charlie    18
# Ellen      24
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.iloc[1::2, 0])
print(type(df.iloc[1::2, 0]))
# name
# Bob      42
# Dave     68
# Frank    30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

df.loc['Bob':'Dave', 'age'] = [20, 30, 40]
print(df.loc['Bob':'Dave', 'age'])
# name
# Bob        20
# Charlie    30
# Dave       40
# Name: age, dtype: int64

print(df['Bob':'Ellen'])
#          age state  point
# name                     
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88

print(df[:3])
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70

print(df['age'])
# name
# Alice      24
# Bob        20
# Charlie    30
# Dave       40
# Ellen      24
# Frank      30
# Name: age, dtype: int64

print(df[['age', 'point']])
#          age  point
# name               
# Alice     24     64
# Bob       20     92
# Charlie   30     70
# Dave      40     70
# Ellen     24     88
# Frank     30     57

print(df.loc['Bob'])
print(type(df.loc['Bob']))
# age      20
# state    CA
# point    92
# Name: Bob, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[[1, 4]])
print(type(df.iloc[[1, 4]]))
#        age state  point
# name                   
# Bob     20    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[:, 'age':'point'])
print(type(df.loc[:, 'age':'point']))
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, [0, 2]])
print(type(df.iloc[:, [0, 2]]))
#          age  point
# name               
# Alice     24     64
# Bob       20     92
# Charlie   30     70
# Dave      40     70
# Ellen     24     88
# Frank     30     57
# <class 'pandas.core.frame.DataFrame'>

print(df.loc['Bob'])
print(type(df.loc['Bob']))
# age      20
# state    CA
# point    92
# Name: Bob, dtype: object
# <class 'pandas.core.series.Series'>

print(df.loc['Bob':'Bob'])
print(type(df.loc['Bob':'Bob']))
#       age state  point
# name                  
# Bob    20    CA     92
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[['Bob']])
print(type(df.loc[['Bob']]))
#       age state  point
# name                  
# Bob    20    CA     92
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, 1])
print(type(df.iloc[:, 1]))
# name
# Alice      NY
# Bob        CA
# Charlie    CA
# Dave       TX
# Ellen      CA
# Frank      NY
# Name: state, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[:, 1:2])
print(type(df.iloc[:, 1:2]))
#         state
# name         
# Alice      NY
# Bob        CA
# Charlie    CA
# Dave       TX
# Ellen      CA
# Frank      NY
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, [1]])
print(type(df.iloc[:, [1]]))
#         state
# name         
# Alice      NY
# Bob        CA
# Charlie    CA
# Dave       TX
# Ellen      CA
# Frank      NY
# <class 'pandas.core.frame.DataFrame'>

l_bool = [True, False, False, True, False, True]

print(df.loc[l_bool, ['age', 'point']])
#        age  point
# name             
# Alice   24     64
# Dave    40     70
# Frank   30     57

print(df.iloc[l_bool, [0, 2]])
#        age  point
# name             
# Alice   24     64
# Dave    40     70
# Frank   30     57

l_bool_wrong = [True, False, False]

# print(df.loc[l_bool_wrong, ['age', 'point']])
# IndexError: Boolean index has wrong length: 3 instead of 6

s_bool = pd.Series([True, False, True, True, False, False],
                   index=reversed(df.index))
print(s_bool)
# Frank       True
# Ellen      False
# Dave        True
# Charlie     True
# Bob        False
# Alice      False
# dtype: bool

print(df.loc[s_bool, ['age', 'point']])
#          age  point
# name               
# Charlie   30     70
# Dave      40     70
# Frank     30     57

# print(df.iloc[s_bool, [0, 2]])
# ValueError: Location based indexing can only have [integer,
# integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types

s_bool_wrong = pd.Series([True, False, False], index=['Frank', 'Ellen', 'Dave'])
print(s_bool_wrong)
# Frank     True
# Ellen    False
# Dave     False
# dtype: bool

# print(df.loc[s_bool_wrong, ['age', 'point']])
# IndexingError: Unalignable boolean Series provided as indexer
# (index of the boolean Seriesand of the indexed object do not match).

s_bool_wrong2 = pd.Series([True, False, False, True, False, True],
                          index=['A', 'B', 'C', 'D', 'E', 'F'])
print(s_bool_wrong2)
# A     True
# B    False
# C    False
# D     True
# E    False
# F     True
# dtype: bool

# print(df.loc[s_bool_wrong2, ['age', 'point']])
# IndexingError: Unalignable boolean Series provided as indexer
# (index of the boolean Series and of the indexed object do not match).

df_duplicated = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=2)
df_duplicated.columns = ['name', 'age', 'age']
print(df_duplicated)
#           name  age  age
# state                   
# NY       Alice   24   64
# CA         Bob   42   92
# CA     Charlie   18   70
# TX        Dave   68   70
# CA       Ellen   24   88
# NY       Frank   30   57

print(df_duplicated.at['NY', 'age'])
print(type(df_duplicated.at['NY', 'age']))
#        age  age
# state          
# NY      24   64
# NY      30   57
# <class 'pandas.core.frame.DataFrame'>

print(df_duplicated.loc['NY', 'age'])
print(type(df_duplicated.loc['NY', 'age']))
#        age  age
# state          
# NY      24   64
# NY      30   57
# <class 'pandas.core.frame.DataFrame'>

print(df_duplicated.iat[0, 1])
# 24

print(df_duplicated.iloc[:2, [0, 1]])
#         name  age
# state            
# NY     Alice   24
# CA       Bob   42

print(df_duplicated.index.is_unique)
# False

print(df_duplicated.columns.is_unique)
# False

print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.index[2])
# Charlie

print(df.columns[1])
# state

print(df.index[2:4])
# Index(['Charlie', 'Dave'], dtype='object', name='name')

print(df.columns[[0, 2]])
# Index(['age', 'point'], dtype='object')

print(df.at[df.index[2], 'age'])
# 30

print(df.loc[['Alice', 'Dave'], df.columns[[0, 2]]])
#        age  point
# name             
# Alice   24     64
# Dave    40     70

print(df['age'][2])
# 30

print(df.loc[['Alice', 'Dave']].iloc[:, [0, 2]])
#        age  point
# name             
# Alice   24     64
# Dave    40     70
