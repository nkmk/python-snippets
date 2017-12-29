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

df_new = df.drop(2, axis=0)
print(df_new)
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57

df_new = df.drop(2)
print(df_new)
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57

df_new = df.drop(index=2)
print(df_new)
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57

df_new = df.drop([0, 2, 4])
print(df_new)
#     name  age state  point
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

df_new = df.drop(index=[0, 2, 4])
print(df_new)
#     name  age state  point
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

df_org = df.copy()
df_org.drop(index=[0, 2, 4], inplace=True)
print(df_org)
#     name  age state  point
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

df2 = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
print(df2)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

df_new = df2.drop(index=['Bob', 'Dave', 'Frank'])
print(df_new)
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Ellen     24    CA     88

df_new = df.drop('state', axis=1)
print(df_new)
#       name  age  point
# 0    Alice   24     64
# 1      Bob   42     92
# 2  Charlie   18     70
# 3     Dave   68     70
# 4    Ellen   24     88
# 5    Frank   30     57

df_new = df.drop(columns='state')
print(df_new)
#       name  age  point
# 0    Alice   24     64
# 1      Bob   42     92
# 2  Charlie   18     70
# 3     Dave   68     70
# 4    Ellen   24     88
# 5    Frank   30     57

df_new = df.drop(['state', 'point'], axis=1)
print(df_new)
#       name  age
# 0    Alice   24
# 1      Bob   42
# 2  Charlie   18
# 3     Dave   68
# 4    Ellen   24
# 5    Frank   30

df_new = df.drop(columns=['state', 'point'])
print(df_new)
#       name  age
# 0    Alice   24
# 1      Bob   42
# 2  Charlie   18
# 3     Dave   68
# 4    Ellen   24
# 5    Frank   30

df_org = df.copy()
df_org.drop(columns=['state', 'point'], inplace=True)
print(df_org)
#       name  age
# 0    Alice   24
# 1      Bob   42
# 2  Charlie   18
# 3     Dave   68
# 4    Ellen   24
# 5    Frank   30

df_new = df.drop(index=[0, 2, 4], columns=['state', 'point'])
print(df_new)
#     name  age
# 1    Bob   42
# 3   Dave   68
# 5  Frank   30

df_org = df.copy()
df_org.drop(index=[0, 2, 4], columns=['state', 'point'], inplace=True)
print(df_org)
#     name  age
# 1    Bob   42
# 3   Dave   68
# 5  Frank   30
