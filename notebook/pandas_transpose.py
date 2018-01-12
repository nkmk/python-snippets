import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

df_t = df.T
print(df_t)
#            0    1        2
# name   Alice  Bob  Charlie
# age       24   42       18
# state     NY   CA       CA
# point     64   92       70

df_tr = df.transpose()
print(df_tr)
#            0    1        2
# name   Alice  Bob  Charlie
# age       24   42       18
# state     NY   CA       CA
# point     64   92       70

df = df.T
print(df)
#            0    1        2
# name   Alice  Bob  Charlie
# age       24   42       18
# state     NY   CA       CA
# point     64   92       70
