import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.read_csv('data/src/sample_pandas_normal.csv').sort_values('state')
print(df)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

print(df.reset_index())
#    index     name  age state  point
# 0      1      Bob   42    CA     92
# 1      2  Charlie   18    CA     70
# 2      4    Ellen   24    CA     88
# 3      0    Alice   24    NY     64
# 4      5    Frank   30    NY     57
# 5      3     Dave   68    TX     70

print(df.reset_index(drop=True))
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70

df.reset_index(inplace=True, drop=True)
print(df)
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70

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

print(df_name.reset_index())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df_name.set_index('state'))
#        age  point
# state            
# NY      24     64
# CA      42     92
# CA      18     70
# TX      68     70
# CA      24     88
# NY      30     57

print(df_name.reset_index().set_index('state'))
#           name  age  point
# state                     
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

df_mi = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=(2, 0))
print(df_mi)
#                age  point
# state name               
# NY    Alice     24     64
# CA    Bob       42     92
#       Charlie   18     70
# TX    Dave      68     70
# CA    Ellen     24     88
# NY    Frank     30     57

print(df_mi.reset_index())
#   state     name  age  point
# 0    NY    Alice   24     64
# 1    CA      Bob   42     92
# 2    CA  Charlie   18     70
# 3    TX     Dave   68     70
# 4    CA    Ellen   24     88
# 5    NY    Frank   30     57

print(df_mi.reset_index(level='state'))
#         state  age  point
# name                     
# Alice      NY   24     64
# Bob        CA   42     92
# Charlie    CA   18     70
# Dave       TX   68     70
# Ellen      CA   24     88
# Frank      NY   30     57
