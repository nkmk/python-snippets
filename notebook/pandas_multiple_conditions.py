import pandas as pd

print(pd.__version__)
# 2.0.3

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
print(df[mask])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df['age'] < 25)
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# Name: age, dtype: bool

print(df[df['age'] < 25])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# 3     True
# 4    False
# 5    False
# Name: name, dtype: bool

print(df[df['name'].str.endswith('e')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

print((df['age'] < 25) & df['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# 3    False
# 4    False
# 5    False
# dtype: bool

print(df[(df['age'] < 25) & df['name'].str.endswith('e')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(~df['name'].str.endswith('e'))
# 0    False
# 1     True
# 2    False
# 3    False
# 4     True
# 5     True
# Name: name, dtype: bool

print(df['point'] < 65)
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# Name: point, dtype: bool

print(~df['name'].str.endswith('e') | (df['point'] < 65))
# 0     True
# 1     True
# 2    False
# 3    False
# 4     True
# 5     True
# dtype: bool

print(df[~df['name'].str.endswith('e') | (df['point'] < 65)])
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57

print(df['state'].isin(['NY', 'TX']))
# 0     True
# 1    False
# 2    False
# 3     True
# 4    False
# 5     True
# Name: state, dtype: bool

print(df[df['state'].isin(['NY', 'TX'])])
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df[(df['state'] == 'NY') | (df['state'] == 'TX')])
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df[df['name'].str.contains('li') | df['name'].str.endswith('k')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 5    Frank   30    NY     57

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
