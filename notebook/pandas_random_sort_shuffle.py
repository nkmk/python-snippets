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

df_s = df.sample(frac=1)
print(df_s)
#       name  age state  point
# 2  Charlie   18    CA     70
# 5    Frank   30    NY     57
# 4    Ellen   24    CA     88
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64
# 3     Dave   68    TX     70

df_s = df.sample(frac=1, random_state=0)
print(df_s)
#       name  age state  point
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88

df_s = df.sample(frac=1).reset_index(drop=True)
print(df_s)
#       name  age state  point
# 0    Ellen   24    CA     88
# 1  Charlie   18    CA     70
# 2    Alice   24    NY     64
# 3     Dave   68    TX     70
# 4    Frank   30    NY     57
# 5      Bob   42    CA     92

df = df.sample(frac=1).reset_index(drop=True)
print(df)
#       name  age state  point
# 0     Dave   68    TX     70
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
