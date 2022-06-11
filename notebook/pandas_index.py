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

print(df['age'])
print(type(df['age']))
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.age)
print(type(df.age))
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df[['point', 'age']])
print(type(df[['point', 'age']]))
#          point  age
# name               
# Alice       64   24
# Bob         92   42
# Charlie     70   18
# Dave        70   68
# Ellen       88   24
# Frank       57   30
# <class 'pandas.core.frame.DataFrame'>

print(df[['age']])
print(type(df[['age']]))
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[:, 'age':'state'])
print(type(df.loc[:, 'age':'state']))
#          age state
# name              
# Alice     24    NY
# Bob       42    CA
# Charlie   18    CA
# Dave      68    TX
# Ellen     24    CA
# Frank     30    NY
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, [2, 0]])
print(type(df.iloc[:, [2, 0]]))
#          point  age
# name               
# Alice       64   24
# Bob         92   42
# Charlie     70   18
# Dave        70   68
# Ellen       88   24
# Frank       57   30
# <class 'pandas.core.frame.DataFrame'>

print(df[1:4])
print(type(df[1:4]))
#          age state  point
# name                     
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# <class 'pandas.core.frame.DataFrame'>

print(df[:-3])
print(type(df[:-3]))
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# <class 'pandas.core.frame.DataFrame'>

print(df[::2])
print(type(df[::2]))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df[1::2])
print(type(df[1::2]))
#        age state  point
# name                   
# Bob     42    CA     92
# Dave    68    TX     70
# Frank   30    NY     57
# <class 'pandas.core.frame.DataFrame'>

# print(df[1])
# KeyError: 1

print(df[1:2])
print(type(df[1:2]))
#       age state  point
# name                  
# Bob    42    CA     92
# <class 'pandas.core.frame.DataFrame'>

print(df['Bob':'Ellen'])
print(type(df['Bob':'Ellen']))
#          age state  point
# name                     
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.loc['Bob'])
print(type(df.loc['Bob']))
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object
# <class 'pandas.core.series.Series'>

print(df.loc[['Bob', 'Ellen']])
print(type(df.loc[['Bob', 'Ellen']]))
#        age state  point
# name                   
# Bob     42    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[[1, 4]])
print(type(df.iloc[[1, 4]]))
#        age state  point
# name                   
# Bob     42    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df['age']['Alice'])
# 24

print(df['Bob':'Dave'][['age', 'point']])
#          age  point
# name               
# Bob       42     92
# Charlie   18     70
# Dave      68     70

print(df.at['Alice', 'age'])
# 24

print(df.loc['Bob':'Dave', ['age', 'point']])
#          age  point
# name               
# Bob       42     92
# Charlie   18     70
# Dave      68     70
