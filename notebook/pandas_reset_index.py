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

df.sort_values('state', inplace=True)
print(df)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

df_r = df.reset_index()
print(df_r)
#    index     name  age state  point
# 0      1      Bob   42    CA     92
# 1      2  Charlie   18    CA     70
# 2      4    Ellen   24    CA     88
# 3      0    Alice   24    NY     64
# 4      5    Frank   30    NY     57
# 5      3     Dave   68    TX     70

df_r = df.reset_index(drop=True)
print(df_r)
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70

df.reset_index(inplace=True, drop=True)
print(df)
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70
