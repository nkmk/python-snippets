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

print(df.sort_values('age'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

print(df.sort_values('state'))
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

print(df.sort_values(['age', 'state']))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

print(df.sort_values(['state', 'age']))
#       name  age state  point
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

print(df.sort_values('age', ascending=False))
#       name  age state  point
# 3     Dave   68    TX     70
# 1      Bob   42    CA     92
# 5    Frank   30    NY     57
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 2  Charlie   18    CA     70

print(df.sort_values(['age', 'state'], ascending=False))
#       name  age state  point
# 3     Dave   68    TX     70
# 1      Bob   42    CA     92
# 5    Frank   30    NY     57
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 2  Charlie   18    CA     70

print(df.sort_values(['age', 'state'], ascending=[True, False]))
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

print(df.sort_values('age', ignore_index=True))
#       name  age state  point
# 0  Charlie   18    CA     70
# 1    Alice   24    NY     64
# 2    Ellen   24    CA     88
# 3    Frank   30    NY     57
# 4      Bob   42    CA     92
# 5     Dave   68    TX     70

df_nan = df.copy()
df_nan.iloc[0, 1] = float('nan')
df_nan.iloc[4, 1] = float('nan')
print(df_nan)
#       name   age state  point
# 0    Alice   NaN    NY     64
# 1      Bob  42.0    CA     92
# 2  Charlie  18.0    CA     70
# 3     Dave  68.0    TX     70
# 4    Ellen   NaN    CA     88
# 5    Frank  30.0    NY     57

print(df_nan.sort_values('age'))
#       name   age state  point
# 2  Charlie  18.0    CA     70
# 5    Frank  30.0    NY     57
# 1      Bob  42.0    CA     92
# 3     Dave  68.0    TX     70
# 0    Alice   NaN    NY     64
# 4    Ellen   NaN    CA     88

print(df_nan.sort_values('age', na_position='first'))
#       name   age state  point
# 0    Alice   NaN    NY     64
# 4    Ellen   NaN    CA     88
# 2  Charlie  18.0    CA     70
# 5    Frank  30.0    NY     57
# 1      Bob  42.0    CA     92
# 3     Dave  68.0    TX     70

print(df.sort_values('name', key=lambda s: s.str.len()))
#       name  age state  point
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70

# print(df.sort_values('name', key=len))
# TypeError: object of type 'int' has no len()

print(df.sort_values('name', key=lambda s: s.map(len)))
#       name  age state  point
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70

df_num = df.select_dtypes('number')
print(df_num)
#    age  point
# 0   24     64
# 1   42     92
# 2   18     70
# 3   68     70
# 4   24     88
# 5   30     57

print(df_num.sort_values(1, axis=1, ascending=False))
#    point  age
# 0     64   24
# 1     92   42
# 2     70   18
# 3     70   68
# 4     88   24
# 5     57   30

df_copy = df.copy()
df_copy.sort_values('age', inplace=True)
print(df_copy)
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

df_sorted = df.sort_values('age')
print(df_sorted)
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

print(df_sorted.sort_index())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.sort_index(axis=1))
#    age     name  point state
# 0   24    Alice     64    NY
# 1   42      Bob     92    CA
# 2   18  Charlie     70    CA
# 3   68     Dave     70    TX
# 4   24    Ellen     88    CA
# 5   30    Frank     57    NY

print(df.sort_index(axis=1, ascending=False, key=lambda s: s.str.len()))
#   state  point     name  age
# 0    NY     64    Alice   24
# 1    CA     92      Bob   42
# 2    CA     70  Charlie   18
# 3    TX     70     Dave   68
# 4    CA     88    Ellen   24
# 5    NY     57    Frank   30
