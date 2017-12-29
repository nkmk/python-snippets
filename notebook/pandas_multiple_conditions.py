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

mask = [True, False, True, False, True, False]
df_mask = df[mask]
print(df_mask)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df['age'] < 35)
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# 5     True
# Name: age, dtype: bool

print(~(df['state'] == 'NY'))
# 0    False
# 1     True
# 2     True
# 3     True
# 4     True
# 5    False
# Name: state, dtype: bool

print((df['age'] < 35) & ~(df['state'] == 'NY'))
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# dtype: bool

df_and = df[(df['age'] < 35) & ~(df['state'] == 'NY')]
print(df_and)
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print((df['age'] < 20) | (df['point'] > 90))
# 0    False
# 1     True
# 2     True
# 3    False
# 4    False
# 5    False
# dtype: bool

df_or = df[(df['age'] < 20) | (df['point'] > 90)]
print(df_or)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

df_multi_1 = df[(df['age'] < 35) | ~(df['state'] == 'NY') & (df['point'] < 75)]
print(df_multi_1)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_multi_2 = df[(df['age'] < 35) & (df['point'] < 75) | ~(df['state'] == 'NY')]
print(df_multi_2)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_multi_3 = df[((df['age'] < 35) | ~(df['state'] == 'NY')) & (df['point'] < 75)]
print(df_multi_3)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 5    Frank   30    NY     57
