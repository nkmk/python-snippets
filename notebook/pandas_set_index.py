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

df_id = df.set_index('name', drop=False)
print(df_id)
#             name  age state  point
# name                              
# Alice      Alice   24    NY     64
# Bob          Bob   42    CA     92
# Charlie  Charlie   18    CA     70
# Dave        Dave   68    TX     70
# Ellen      Ellen   24    CA     88
# Frank      Frank   30    NY     57

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

print(df_i)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

df_ii = df_i.set_index('state')
print(df_ii)
#        age  point
# state            
# NY      24     64
# CA      42     92
# CA      18     70
# TX      68     70
# CA      24     88
# NY      30     57

df_mi = df_i.set_index('state', append=True)
print(df_mi)
#                age  point
# name    state            
# Alice   NY      24     64
# Bob     CA      42     92
# Charlie CA      18     70
# Dave    TX      68     70
# Ellen   CA      24     88
# Frank   NY      30     57

print(df_mi.swaplevel(0, 1))
#                age  point
# state name               
# NY    Alice     24     64
# CA    Bob       42     92
#       Charlie   18     70
# TX    Dave      68     70
# CA    Ellen     24     88
# NY    Frank     30     57

print(df_i)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

df_ri = df_i.reset_index()
print(df_ri)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_change = df_i.reset_index().set_index('state')
print(df_change)
#           name  age  point
# state                     
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

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
