import pandas as pd

with open('data/src/sample_pandas_normal.csv') as f:
    print(f.read())
# name,age,state,point
# Alice,24,NY,64
# Bob,42,CA,92
# Charlie,18,CA,70
# Dave,68,TX,70
# Ellen,24,CA,88
# Frank,30,NY,57

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

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
# name
# Alice      24
# Bob        42
# Charlie    18
# Dave       68
# Ellen      24
# Frank      30
# Name: age, dtype: int64

print(df.at['Bob', 'age'])
# 42

print(df.query('state == "NY"'))
#        age state  point
# name                   
# Alice   24    NY     64
# Frank   30    NY     57

print(df.query('age > 30'))
#       age state  point
# name                  
# Bob    42    CA     92
# Dave   68    TX     70

print(df.describe())
#              age      point
# count   6.000000   6.000000
# mean   34.333333  73.500000
# std    18.392027  13.707662
# min    18.000000  57.000000
# 25%    24.000000  65.500000
# 50%    27.000000  70.000000
# 75%    39.000000  83.500000
# max    68.000000  92.000000
