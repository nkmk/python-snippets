import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.set_index('name'))
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.set_index('name', drop=False))
#             name  age state  point
# name                              
# Alice      Alice   24    NY     64
# Bob          Bob   42    CA     92
# Charlie  Charlie   18    CA     70
# Dave        Dave   68    TX     70
# Ellen      Ellen   24    CA     88
# Frank      Frank   30    NY     57

print(df.set_index(['state', 'name']))
#                age  point
# state name               
# NY    Alice     24     64
# CA    Bob       42     92
#       Charlie   18     70
# TX    Dave      68     70
# CA    Ellen     24     88
# NY    Frank     30     57

print(df.set_index(['state', 'name']).sort_index())
#                age  point
# state name               
# CA    Bob       42     92
#       Charlie   18     70
#       Ellen     24     88
# NY    Alice     24     64
#       Frank     30     57
# TX    Dave      68     70

df_name = df.set_index('name')
print(df_name)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df_name.set_index('state'))
#        age  point
# state            
# NY      24     64
# CA      42     92
# CA      18     70
# TX      68     70
# CA      24     88
# NY      30     57

df_mi = df_name.set_index('state', append=True)
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

print(df_name.reset_index())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df_name.reset_index().set_index('state'))
#           name  age  point
# state                     
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

print(df.set_index('state'))
#           name  age  point
# state                     
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

# print(df.set_index('state', verify_integrity=True))
# ValueError: Index has duplicate keys: Index(['CA', 'NY'], dtype='object', name='state')

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

df_name = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
print(df_name)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df_name.loc['Bob'])
# age      42
# state    CA
# point    92
# Name: Bob, dtype: object

print(df_name.at['Bob', 'age'])
# 42
