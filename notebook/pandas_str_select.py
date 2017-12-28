import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

mask = [True, False, True]
df_mask = df[mask]
print(df_mask)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['state'] == 'CA')
# 0    False
# 1     True
# 2     True
# Name: state, dtype: bool

df_exact = df[df['state'] == 'CA']
print(df_exact)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df['name'].str.contains('l'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

df_contains = df[df['name'].str.contains('l')]
print(df_contains)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

df_endswith = df[df['name'].str.endswith('e')]
print(df_endswith)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['name'].str.startswith('B'))
# 0    False
# 1     True
# 2    False
# Name: name, dtype: bool

df_startswith = df[df['name'].str.startswith('B')]
print(df_startswith)
#   name  age state  point
# 1  Bob   42    CA     92

print(df['name'].str.match('.*i.*e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

df_match = df[df['name'].str.match('.*i.*e')]
print(df_match)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
