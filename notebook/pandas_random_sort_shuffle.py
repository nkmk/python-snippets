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

print(df.sample(frac=1))
#       name  age state  point
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 4    Ellen   24    CA     88

print(df.sample(frac=1, random_state=0))
#       name  age state  point
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88

print(df.sample(frac=1, random_state=0))
#       name  age state  point
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88

print(df.sample(frac=1, ignore_index=True))
#       name  age state  point
# 0    Ellen   24    CA     88
# 1    Frank   30    NY     57
# 2      Bob   42    CA     92
# 3     Dave   68    TX     70
# 4    Alice   24    NY     64
# 5  Charlie   18    CA     70

print(df.sample(frac=1).reset_index(drop=True))
#       name  age state  point
# 0      Bob   42    CA     92
# 1     Dave   68    TX     70
# 2    Alice   24    NY     64
# 3  Charlie   18    CA     70
# 4    Frank   30    NY     57
# 5    Ellen   24    CA     88

df = df.sample(frac=1)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 4    Ellen   24    CA     88
# 3     Dave   68    TX     70
# 2  Charlie   18    CA     70
