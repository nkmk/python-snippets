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

print(df.query('not age < 25'))
#     name  age state  point
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70
# 5  Frank   30    NY     57

print(df.query('24 <= age < 50'))
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88
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

print(df.query('state != "CA"'))
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

print(df.query('name.str.endswith("e")', engine='python'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

print(df.query('name.str.contains("li")', engine='python'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df.query('name.str.match(".*i.*e")', engine='python'))
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df.query('age.astype("str").str.endswith("8")', engine='python'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

df.at[0, 'name'] = None
print(df)
#       name  age state  point
# 0     None   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

# print(df.query('name.str.endswith("e")', engine='python'))
# ValueError: cannot index with vector containing NA / NaN values

print(df[df['name'].str.endswith('e', na=False)])
#       name  age state  point
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70

# print(df.query('name.str.endswith("e", na=False)', engine='python'))
# AttributeError: 'dict' object has no attribute 'append'

df['name'].fillna('Alice', inplace=True)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

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

print(df_name.query('name.str.endswith("e")', engine='python'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70

print(df_name.query('index.str.endswith("e")', engine='python'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70

val = 80
print(df.query('point > @val'))
#     name  age state  point
# 1    Bob   42    CA     92
# 4  Ellen   24    CA     88

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

print(df.query('age < 25 | point > 65'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88

print(df.query('age < 25 or point > 65'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
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

df.columns = ['名前', 'age.year', 'state name', 3]
print(df)
#         名前  age.year state name   3
# 0    Alice        24         NY  64
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 3     Dave        68         TX  70
# 4    Ellen        24         CA  88
# 5    Frank        30         NY  57

print(df.query('名前 == ["Alice", "Dave"]'))
#       名前  age.year state name   3
# 0  Alice        24         NY  64
# 3   Dave        68         TX  70

print(df.query('名前.str.contains("li")', engine='python'))
#         名前  age.year state name   3
# 0    Alice        24         NY  64
# 2  Charlie        18         CA  70

# print(df.query('age.year < 25'))
# UndefinedVariableError: name 'age' is not defined

# print(df.query('state name == "CA"'))
# SyntaxError: invalid syntax

# print(df.query('3 > 75'))
# KeyError: False

print(df[df['age.year'] < 25])
#         名前  age.year state name   3
# 0    Alice        24         NY  64
# 2  Charlie        18         CA  70
# 4    Ellen        24         CA  88

print(df[df['state name'] == 'CA'])
#         名前  age.year state name   3
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 4    Ellen        24         CA  88

print(df[df[3] > 75])
#       名前  age.year state name   3
# 1    Bob        42         CA  92
# 4  Ellen        24         CA  88

df.rename(columns={'3': 'point'}, inplace=True)
print(df)
#         名前  age.year state name   3
# 0    Alice        24         NY  64
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 3     Dave        68         TX  70
# 4    Ellen        24         CA  88
# 5    Frank        30         NY  57

df.columns = [str(s).replace(' ', '_').replace('.', '_') for s in df.columns]
print(df)
#         名前  age_year state_name   3
# 0    Alice        24         NY  64
# 1      Bob        42         CA  92
# 2  Charlie        18         CA  70
# 3     Dave        68         TX  70
# 4    Ellen        24         CA  88
# 5    Frank        30         NY  57

df.query('age_year > 25', inplace=True)
print(df)
#       名前  age_year state_name   3
# 1    Bob        42         CA  92
# 3   Dave        68         TX  70
# 5  Frank        30         NY  57
