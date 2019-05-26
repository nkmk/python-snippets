import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df['name'].str.cat(df['state']))
# 0      AliceNY
# 1        BobCA
# 2    CharlieCA
# Name: name, dtype: object

print(df['name'].str.cat(df['state'], sep=' in '))
# 0      Alice in NY
# 1        Bob in CA
# 2    Charlie in CA
# Name: name, dtype: object

print(df['name'].str.cat(['X', 'Y', 'Z'], sep=' in '))
# 0      Alice in X
# 1        Bob in Y
# 2    Charlie in Z
# Name: name, dtype: object

print(df['name'].str.cat([df['state'], ['X', 'Y', 'Z']], sep='-'))
# 0      Alice-NY-X
# 1        Bob-CA-Y
# 2    Charlie-CA-Z
# Name: name, dtype: object

# print(df['name'].str.cat('X', sep='-'))
# ValueError: Did you mean to supply a `sep` keyword?

print(df['name'] + df['state'])
# 0      AliceNY
# 1        BobCA
# 2    CharlieCA
# dtype: object

print(df['name'] + ' in ' + df['state'])
# 0      Alice in NY
# 1        Bob in CA
# 2    Charlie in CA
# dtype: object

print(df['name'] + ' in ' + df['state'] + ' - ' + ['X', 'Y', 'Z'])
# 0      Alice in NY - X
# 1        Bob in CA - Y
# 2    Charlie in CA - Z
# dtype: object

df['col_NaN'] = ['X', pd.np.nan, 'Z']
print(df)
#       name  age state  point col_NaN
# 0    Alice   24    NY     64       X
# 1      Bob   42    CA     92     NaN
# 2  Charlie   18    CA     70       Z

print(df['name'].str.cat(df['col_NaN'], sep='-'))
# 0      Alice-X
# 1          NaN
# 2    Charlie-Z
# Name: name, dtype: object

print(df['name'].str.cat(df['col_NaN'], sep='-', na_rep='No Data'))
# 0        Alice-X
# 1    Bob-No Data
# 2      Charlie-Z
# Name: name, dtype: object

print(df['name'] + '-' + df['col_NaN'])
# 0      Alice-X
# 1          NaN
# 2    Charlie-Z
# dtype: object

print(df['name'] + '-' + df['col_NaN'].fillna('No Data'))
# 0        Alice-X
# 1    Bob-No Data
# 2      Charlie-Z
# dtype: object

# print(df['name'].str.cat(df['age'], sep='-'))
# TypeError: sequence item 1: expected str instance, int found

print(df['name'].str.cat(df['age'].astype(str), sep='-'))
# 0      Alice-24
# 1        Bob-42
# 2    Charlie-18
# Name: name, dtype: object

# print(df['name'] + '-' + df['age'])
# TypeError: can only concatenate str (not "int") to str

print(df['name'] + '-' + df['age'].astype(str))
# 0      Alice-24
# 1        Bob-42
# 2    Charlie-18
# dtype: object

df['name_state'] = df['name'].str.cat(df['state'], sep=' in ')
print(df)
#       name  age state  point col_NaN     name_state
# 0    Alice   24    NY     64       X    Alice in NY
# 1      Bob   42    CA     92     NaN      Bob in CA
# 2  Charlie   18    CA     70       Z  Charlie in CA

print(df.drop(columns=['name', 'state']))
#    age  point col_NaN     name_state
# 0   24     64       X    Alice in NY
# 1   42     92     NaN      Bob in CA
# 2   18     70       Z  Charlie in CA

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df.assign(name_state=df['name'] + ' in ' + df['state']))
#       name  age state  point     name_state
# 0    Alice   24    NY     64    Alice in NY
# 1      Bob   42    CA     92      Bob in CA
# 2  Charlie   18    CA     70  Charlie in CA

print(df.assign(name_state=df['name'] + ' in ' + df['state']).drop(columns=['name', 'state']))
#    age  point     name_state
# 0   24     64    Alice in NY
# 1   42     92      Bob in CA
# 2   18     70  Charlie in CA
