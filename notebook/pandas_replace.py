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

print(df.replace('CA', 'California'))
#       name  age       state  point
# 0    Alice   24          NY     64
# 1      Bob   42  California     92
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen   24  California     88
# 5    Frank   30          NY     57

print(df.replace({'CA': 'California', 'NY': 'New York'}))
#       name  age       state  point
# 0    Alice   24    New York     64
# 1      Bob   42  California     92
# 2  Charlie   18  California     70
# 3     Dave   68          TX     70
# 4    Ellen   24  California     88
# 5    Frank   30    New York     57

print(df.replace('li', 'LI'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.replace('(.*)li(.*)', r'\1LI\2', regex=True))
#       name  age state  point
# 0    ALIce   24    NY     64
# 1      Bob   42    CA     92
# 2  CharLIe   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df['name'] = df['name'].str.replace('li', 'LI')
print(df)
#       name  age state  point
# 0    ALIce   24    NY     64
# 1      Bob   42    CA     92
# 2  CharLIe   18    CA     70
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
