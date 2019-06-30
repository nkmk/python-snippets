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

df_s = df.sort_values('state')
print(df_s)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

df_s = df.sort_values('state', ascending=False)
print(df_s)
#       name  age state  point
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88

df_s = df.sort_values(['state', 'age'])
print(df_s)
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

df_s = df.sort_values(['age', 'state'])
print(df_s)
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

df_s = df.sort_values(['age', 'state'], ascending=[True, False])
print(df_s)
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

df_nan = df.copy()
df_nan.iloc[:2, 1] = pd.np.nan
print(df_nan)
#       name   age state  point
# 0    Alice   NaN    NY     64
# 1      Bob   NaN    CA     92
# 2  Charlie  18.0    CA     70
# 3     Dave  68.0    TX     70
# 4    Ellen  24.0    CA     88
# 5    Frank  30.0    NY     57

df_nan_s = df_nan.sort_values('age')
print(df_nan_s)
#       name   age state  point
# 2  Charlie  18.0    CA     70
# 4    Ellen  24.0    CA     88
# 5    Frank  30.0    NY     57
# 3     Dave  68.0    TX     70
# 0    Alice   NaN    NY     64
# 1      Bob   NaN    CA     92

df_nan_s = df_nan.sort_values('age', na_position='first')
print(df_nan_s)
#       name   age state  point
# 0    Alice   NaN    NY     64
# 1      Bob   NaN    CA     92
# 2  Charlie  18.0    CA     70
# 4    Ellen  24.0    CA     88
# 5    Frank  30.0    NY     57
# 3     Dave  68.0    TX     70

df.sort_values('state', inplace=True)
print(df)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

df_d = df.drop(['name', 'state'], axis=1)
print(df_d)
#    age  point
# 1   42     92
# 2   18     70
# 4   24     88
# 0   24     64
# 5   30     57
# 3   68     70

df_d .sort_values(by=1, axis=1, ascending=False, inplace=True)
print(df_d)
#    point  age
# 1     92   42
# 2     70   18
# 4     88   24
# 0     64   24
# 5     57   30
# 3     70   68

print(df)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

df_s = df.sort_index()
print(df_s)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_s = df.sort_index(ascending=False)
print(df_s)
#       name  age state  point
# 5    Frank   30    NY     57
# 4    Ellen   24    CA     88
# 3     Dave   68    TX     70
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64

df.sort_index(inplace=True)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_s = df.sort_index(axis=1)
print(df_s)
#    age     name  point state
# 0   24    Alice     64    NY
# 1   42      Bob     92    CA
# 2   18  Charlie     70    CA
# 3   68     Dave     70    TX
# 4   24    Ellen     88    CA
# 5   30    Frank     57    NY

df.sort_index(axis=1, ascending=False, inplace=True)
print(df)
#   state  point     name  age
# 0    NY     64    Alice   24
# 1    CA     92      Bob   42
# 2    CA     70  Charlie   18
# 3    TX     70     Dave   68
# 4    CA     88    Ellen   24
# 5    NY     57    Frank   30
