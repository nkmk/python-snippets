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

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
df_t = df.T

df.at[0, 'age'] = 100

print(df)
#       name  age state  point
# 0    Alice  100    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

print(df_t)
#            0    1        2
# name   Alice  Bob  Charlie
# age       24   42       18
# state     NY   CA       CA
# point     64   92       70

df_ = pd.DataFrame(pd.np.arange(6).reshape(2, 3))
print(df_)
#    0  1  2
# 0  0  1  2
# 1  3  4  5

df_t_ = df_.T
print(df_t_)
#    0  1
# 0  0  3
# 1  1  4
# 2  2  5

df_.iat[0, 0] = 100

print(df_)
#      0  1  2
# 0  100  1  2
# 1    3  4  5

print(df_t_)
#      0  1
# 0  100  3
# 1    1  4
# 2    2  5

df_ = pd.DataFrame(pd.np.arange(6).reshape(2, 3))
df_t_copy = df_.T.copy()

df_.iat[0, 0] = 100

print(df_)
#      0  1  2
# 0  100  1  2
# 1    3  4  5

print(df_t_copy)
#    0  1
# 0  0  3
# 1  1  4
# 2  2  5

df_ = pd.DataFrame(pd.np.arange(6).reshape(2, 3))
df_t_copy = df_.transpose(copy=True)

df_.iat[0, 0] = 100

print(df_)
#      0  1  2
# 0  100  1  2
# 1    3  4  5

print(df_t_copy)
#    0  1
# 0  0  3
# 1  1  4
# 2  2  5
