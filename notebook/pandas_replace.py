import pandas as pd

print(pd.__version__)
# 2.1.2

df = pd.read_csv('data/src/sample_pandas_normal.csv')
df.iloc[1, 3] = 24
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     24
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.replace('CA', 'California'))
#       name  age       state  point
# 0    Alice   24          NY     64
# 1      Bob   42  California     24
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen   24  California     88
# 5    Frank   30          NY     57

print(df.replace(24, 100))
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA    100
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen  100    CA     88
# 5    Frank   30    NY     57

print(df.replace({'CA': 'California', 24: 100}))
#       name  age       state  point
# 0    Alice  100          NY     64
# 1      Bob   42  California    100
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen  100  California     88
# 5    Frank   30          NY     57

print(df.replace(['CA', 24], ['California', 100]))
#       name  age       state  point
# 0    Alice  100          NY     64
# 1      Bob   42  California    100
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen  100  California     88
# 5    Frank   30          NY     57

# print(df.replace(['CA', 24, 'NY'], ['California', 100]))
# ValueError: Replacement lists must match in length. Expecting 3 got 2

print(df.replace(['CA', 24], 'XXX'))
#       name  age state point
# 0    Alice  XXX    NY    64
# 1      Bob   42   XXX   XXX
# 2  Charlie   18   XXX    70
# 3     Dave   68    TX    70
# 4    Ellen  XXX   XXX    88
# 5    Frank   30    NY    57

print(df.replace({'age': {24: 100}}))
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA     24
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen  100    CA     88
# 5    Frank   30    NY     57

print(df.replace({'age': {24: 100, 18: 0}, 'point': {24: 50}}))
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA     50
# 2  Charlie    0    CA     70
# 3     Dave   68    TX     70
# 4    Ellen  100    CA     88
# 5    Frank   30    NY     57

# print(df.replace({'age': [[24, 18], [100, 0]], 'point': {24: 50}}))
# TypeError: If a nested mapping is passed, all values of the top level mapping must be mappings

print(df.replace({'age': 24, 'point': 70}, 100))
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA     24
# 2  Charlie   18    CA    100
# 3     Dave   68    TX    100
# 4    Ellen  100    CA     88
# 5    Frank   30    NY     57

print(df.replace({'age': [24, 18], 'point': 70}, 100))
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA     24
# 2  Charlie  100    CA    100
# 3     Dave   68    TX    100
# 4    Ellen  100    CA     88
# 5    Frank   30    NY     57

print(df.replace('li', 'XX'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     24
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.replace('.*e$', 'NEW_NAME', regex=True))
#        name  age state  point
# 0  NEW_NAME   24    NY     64
# 1       Bob   42    CA     24
# 2  NEW_NAME   18    CA     70
# 3  NEW_NAME   68    TX     70
# 4     Ellen   24    CA     88
# 5     Frank   30    NY     57

print(df.replace('li', 'XX', regex=True))
#       name  age state  point
# 0    AXXce   24    NY     64
# 1      Bob   42    CA     24
# 2  CharXXe   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.replace('(.*)li(.*)', r'\2-\1', regex=True))
#      name  age state  point
# 0    ce-A   24    NY     64
# 1     Bob   42    CA     24
# 2  e-Char   18    CA     70
# 3    Dave   68    TX     70
# 4   Ellen   24    CA     88
# 5   Frank   30    NY     57

df['name'] = df['name'].str.replace('li', 'XX')
print(df)
#       name  age state  point
# 0    AXXce   24    NY     64
# 1      Bob   42    CA     24
# 2  CharXXe   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df.replace('CA', 'California', inplace=True)
print(df)
#       name  age       state  point
# 0    Alice   24          NY     64
# 1      Bob   42  California     92
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen   24  California     88
# 5    Frank   30          NY     57
