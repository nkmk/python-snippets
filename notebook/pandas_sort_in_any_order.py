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

print(df.sort_values('age'))
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70

print(df.sort_values('name', ascending=False))
#       name  age state  point
# 5    Frank   30    NY     57
# 4    Ellen   24    CA     88
# 3     Dave   68    TX     70
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64

d_order = {'Charlie': 0, 'Alice': 1, 'Ellen': 2, 'Bob': 3}

print(df['name'].map(d_order))
# 0    1.0
# 1    3.0
# 2    0.0
# 3    NaN
# 4    2.0
# 5    NaN
# Name: name, dtype: float64

print(df.sort_values('name', key=lambda col: col.map(d_order)))
#       name  age state  point
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 1      Bob   42    CA     92
# 3     Dave   68    TX     70
# 5    Frank   30    NY     57

print(df.sort_values('name', key=lambda col: col.map(d_order), na_position='first'))
#       name  age state  point
# 3     Dave   68    TX     70
# 5    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 0    Alice   24    NY     64
# 4    Ellen   24    CA     88
# 1      Bob   42    CA     92
