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

df_i = df.set_index('name')
print(df_i)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

df_mi = df.set_index(['state', 'name'])
print(df_mi)
#                age  point
# state name               
# NY    Alice     24     64
# CA    Bob       42     92
#       Charlie   18     70
# TX    Dave      68     70
# CA    Ellen     24     88
# NY    Frank     30     57

df_mi.sort_index(inplace=True)
print(df_mi)
#                age  point
# state name               
# CA    Bob       42     92
#       Charlie   18     70
#       Ellen     24     88
# NY    Alice     24     64
#       Frank     30     57
# TX    Dave      68     70

df.set_index('name', inplace=True)
print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

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

print(df.loc['Bob'])
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object

print(df.at['Bob', 'age'])
# 42
