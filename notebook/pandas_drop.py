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

print(df.drop('Charlie', axis=0))
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92
# Dave    68    TX     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(df.drop('Charlie'))
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92
# Dave    68    TX     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(df.drop(index='Charlie'))
#        age state  point
# name                   
# Alice   24    NY     64
# Bob     42    CA     92
# Dave    68    TX     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(df.drop(['Bob', 'Dave', 'Frank']))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

print(df.drop(index=['Bob', 'Dave', 'Frank']))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

df_org = df.copy()
df_org.drop(index=['Bob', 'Dave', 'Frank'], inplace=True)
print(df_org)
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

print(df.index[[1, 3, 5]])
# Index(['Bob', 'Dave', 'Frank'], dtype='object', name='name')

print(df.drop(df.index[[1, 3, 5]]))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

print(df.drop(index=df.index[[1, 3, 5]]))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

df_noindex = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df_noindex)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df_noindex.index)
# RangeIndex(start=0, stop=6, step=1)

print(df_noindex.drop([1, 3, 5]))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df_noindex.drop(df_noindex.index[[1, 3, 5]]))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

df_noindex_sort = df_noindex.sort_values('state')
print(df_noindex_sort)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

print(df_noindex_sort.index)
# Int64Index([1, 2, 4, 0, 5, 3], dtype='int64')

print(df_noindex_sort.drop([1, 3, 5]))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64

print(df_noindex_sort.drop(df_noindex_sort.index[[1, 3, 5]]))
#     name  age state  point
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57

print(df.drop('state', axis=1))
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

print(df.drop(columns='state'))
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

print(df.drop(['state', 'point'], axis=1))
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30

print(df.drop(columns=['state', 'point']))
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30

df_org = df.copy()
df_org.drop(columns=['state', 'point'], inplace=True)
print(df_org)
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30

print(df.columns[[1, 2]])
# Index(['state', 'point'], dtype='object')

print(df.drop(df.columns[[1, 2]], axis=1))
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30

print(df.drop(columns=df.columns[[1, 2]]))
#          age
# name        
# Alice     24
# Bob       42
# Charlie   18
# Dave      68
# Ellen     24
# Frank     30

print(df.drop(index=['Bob', 'Dave', 'Frank'],
              columns=['state', 'point']))
#          age
# name        
# Alice     24
# Charlie   18
# Ellen     24

print(df.drop(index=df.index[[1, 3, 5]],
              columns=df.columns[[1, 2]]))
#          age
# name        
# Alice     24
# Charlie   18
# Ellen     24

df_org = df.copy()
df_org.drop(index=['Bob', 'Dave', 'Frank'],
            columns=['state', 'point'], inplace=True)
print(df_org)
#          age
# name        
# Alice     24
# Charlie   18
# Ellen     24
