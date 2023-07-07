import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

mask = [True, False, True]
print(df[mask])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['state'] == 'CA')
# 0    False
# 1     True
# 2     True
# Name: state, dtype: bool

print(df[df['state'] == 'CA'])
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df['state'].isin(['NY', 'CA']))
# 0    True
# 1    True
# 2    True
# Name: state, dtype: bool

print(df[df['state'].isin(['NY', 'CA'])])
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df['name'].str.contains('li'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.contains('li')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

df_nan = df.copy()
df_nan.iloc[2, 0] = float('nan')
print(df_nan)
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 2    NaN   18    CA     70

print(df_nan['name'].str.contains('li'))
# 0     True
# 1    False
# 2      NaN
# Name: name, dtype: object

# print(df_nan[df_nan['name'].str.contains('li')])
# ValueError: Cannot mask with non-boolean array containing NA / NaN values

print(df_nan['name'].str.contains('li', na=False))
# 0     True
# 1    False
# 2    False
# Name: name, dtype: bool

print(df_nan['name'].str.contains('li', na=True))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.contains('LI'))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool

print(df['name'].str.contains('LI', case=False))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.contains('i.*e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.contains('i.*e', regex=False))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool

df_q = df.copy()
df_q.iloc[2, 0] += '?'
print(df_q)
#        name  age state  point
# 0     Alice   24    NY     64
# 1       Bob   42    CA     92
# 2  Charlie?   18    CA     70

# print(df_q['name'].str.contains('?'))
# error: nothing to repeat at position 0

print(df_q['name'].str.contains('?', regex=False))
# 0    False
# 1    False
# 2     True
# Name: name, dtype: bool

print(df_q['name'].str.contains(r'\?'))
# 0    False
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.startswith('B'))
# 0    False
# 1     True
# 2    False
# Name: name, dtype: bool

print(df[df['name'].str.startswith('B')])
#   name  age state  point
# 1  Bob   42    CA     92

print(df['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.endswith('e')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['name'].str.match('.*i'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.match('.*i')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['name'].str.match('i.*e'))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool

print(df['name'].str.contains('i.*e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool
