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

print(df.index.values)
# ['Alice' 'Bob' 'Charlie' 'Dave' 'Ellen' 'Frank']

print(df.columns.values)
# ['age' 'state' 'point']

print(df.at['Bob', 'age'])
print(df.at['Dave', 'state'])
# 42
# TX

df.at['Bob', 'age'] = 60
print(df.at['Bob', 'age'])
# 60

print(df.iat[1, 0])
print(df.iat[3, 1])
# 60
# TX

df.iat[1, 0] = 42
print(df.iat[1, 0])
# 42

print(df.loc['Bob', 'age'])
print(df.iloc[3, 1])
# 42
# TX

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

print(df_state.loc['NY', 'age'])
print(type(df_state.loc['NY', 'age']))
# state
# NY    24
# NY    30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df_state.loc['NY', ['age', 'point']])
print(type(df_state.loc['NY', ['age', 'point']]))
#        age  point
# state            
# NY      24     64
# NY      30     57
# <class 'pandas.core.frame.DataFrame'>

print(df_state.iat[0, 1])
# 24

print(df_state.index.is_unique)
# False

print(df_state.columns.is_unique)
# True

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

print(df.at[df.index[2], 'age'])
# 30

print(df.loc[['Alice', 'Dave'], df.columns[1]])
# name
# Alice    NY
# Dave     TX
# Name: state, dtype: object

print(df['age'][2])
# 30

print(df.age[2])
# 30

print(df.loc[['Alice', 'Dave']].iloc[:, 1])
# name
# Alice    NY
# Dave     TX
# Name: state, dtype: object
