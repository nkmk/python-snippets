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

print(df[df['age'] < 25])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('age < 25'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

val = 25
print(df.query('age < @val'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(f'age < {val}')
# age < 25

print(df.query(f'age < {val}'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('30 <= age < 50'))
#     name  age state  point
# 1    Bob   42    CA     92
# 5  Frank   30    NY     57

print(df.query('age < point / 3'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('state == "CA"'))
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

s = 'CA'
print(df.query('state != @s'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

# print(df.query(f'state != {s}'))
# UndefinedVariableError: name 'CA' is not defined

print(df.query(f'state != "{s}"'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df[df['state'].isin(['NY', 'TX'])])
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df.query('state in ["NY", "TX"]'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df.query('state == ["NY", "TX"]'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

l = ['NY', 'TX']
print(df.query('state in @l'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df.query(f'state in {l}'))
#     name  age state  point
# 0  Alice   24    NY     64
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df.query('name.str.endswith("e")'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

print(df.query('name.str.contains("li")'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df.query('age.astype("str").str.endswith("8")'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

df_nan = df.copy()
df_nan.at[0, 'name'] = float('NaN')
print(df_nan)
#       name  age state  point
# 0      NaN   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

# print(df_nan.query('name.str.endswith("e")'))
# ValueError: unknown type object

print(df_nan[df_nan['name'].str.endswith('e', na=False)])
#       name  age state  point
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

print(df_nan.query('name.str.endswith("e", na=False)'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

print(df.query('index % 2 == 0'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

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

print(df_name.query('name.str.endswith("e")'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70

print(df_name.query('index.str.endswith("e")'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70

print(df[(df['age'] < 25) & (df['point'] > 65)])
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('age < 25 & point > 65'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('age < 25 and point > 65'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('age < 20 | point > 80'))
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('age < 20 or point > 80'))
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

print(df.query('not age < 25 and not point > 65'))
#     name  age state  point
# 5  Frank   30    NY     57

print(df.query('age == 24 | point > 80 & state == "CA"'))
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88

print(df.query('(age == 24 | point > 80) & state == "CA"'))
#     name  age state  point
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88

df_rename = df.set_axis(['0name', 'age.year', 'state name', 3], axis=1)
print(df_rename)
#      0name  age.year state name   3
# 0    Alice        24         NY  64
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 3     Dave        68         TX  70
# 4    Ellen        24         CA  88
# 5    Frank        30         NY  57

# print(df_rename.query('0name.str.endswith("e")'))
# SyntaxError: invalid syntax

# print(df_rename.query('age.year < 25'))
# UndefinedVariableError: name 'age' is not defined

# print(df_rename.query('state name == "CA"'))
# SyntaxError: invalid syntax

print(df_rename.query('`0name`.str.endswith("e")'))
#      0name  age.year state name   3
# 0    Alice        24         NY  64
# 2  Charlie        18         CA  70
# 3     Dave        68         TX  70

print(df_rename.query('`age.year` < 25'))
#      0name  age.year state name   3
# 0    Alice        24         NY  64
# 2  Charlie        18         CA  70
# 4    Ellen        24         CA  88

print(df_rename.query('`state name` == "CA"'))
#      0name  age.year state name   3
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 4    Ellen        24         CA  88

# print(df_rename.query('3 > 75'))
# KeyError: False

# print(df_rename.query('`3` > 75'))
# UndefinedVariableError: name 'BACKTICK_QUOTED_STRING_3' is not defined

print(df_rename[df_rename[3] > 75])
#    0name  age.year state name   3
# 1    Bob        42         CA  92
# 4  Ellen        24         CA  88

df.query('age > 25', inplace=True)
print(df)
#     name  age state  point
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57
