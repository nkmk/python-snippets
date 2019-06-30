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

print(df.sort_values('name'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.sort_values('name', ascending=False))
#       name  age state  point
# 5    Frank   30    NY     57
# 4    Ellen   24    CA     88
# 3     Dave   68    TX     70
# 2  Charlie   18    CA     70
# 1      Bob   42    CA     92
# 0    Alice   24    NY     64

l_order = ['Charlie', 'Alice', 'Dave', 'Bob']

df['order'] = df['name'].apply(lambda x: l_order.index(x) if x in l_order else -1)
print(df)
#       name  age state  point  order
# 0    Alice   24    NY     64      1
# 1      Bob   42    CA     92      3
# 2  Charlie   18    CA     70      0
# 3     Dave   68    TX     70      2
# 4    Ellen   24    CA     88     -1
# 5    Frank   30    NY     57     -1

print(df.sort_values('order'))
#       name  age state  point  order
# 4    Ellen   24    CA     88     -1
# 5    Frank   30    NY     57     -1
# 2  Charlie   18    CA     70      0
# 0    Alice   24    NY     64      1
# 3     Dave   68    TX     70      2
# 1      Bob   42    CA     92      3

print(df.sort_values('order').reset_index(drop=True).drop(columns='order'))
#       name  age state  point
# 0    Ellen   24    CA     88
# 1    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 3    Alice   24    NY     64
# 4     Dave   68    TX     70
# 5      Bob   42    CA     92

d_order = {'Charlie': 0, 'Alice': 1, 'Dave': 2, 'Bob': 3}

df['order'] = df['name'].map(d_order)
print(df)
#       name  age state  point  order
# 0    Alice   24    NY     64    1.0
# 1      Bob   42    CA     92    3.0
# 2  Charlie   18    CA     70    0.0
# 3     Dave   68    TX     70    2.0
# 4    Ellen   24    CA     88    NaN
# 5    Frank   30    NY     57    NaN

print(df.sort_values('order'))
#       name  age state  point  order
# 2  Charlie   18    CA     70    0.0
# 0    Alice   24    NY     64    1.0
# 3     Dave   68    TX     70    2.0
# 1      Bob   42    CA     92    3.0
# 4    Ellen   24    CA     88    NaN
# 5    Frank   30    NY     57    NaN

print(df.sort_values('order', na_position='first'))
#       name  age state  point  order
# 4    Ellen   24    CA     88    NaN
# 5    Frank   30    NY     57    NaN
# 2  Charlie   18    CA     70    0.0
# 0    Alice   24    NY     64    1.0
# 3     Dave   68    TX     70    2.0
# 1      Bob   42    CA     92    3.0

print(df.sort_values('order', na_position='first').reset_index(drop=True).drop(columns='order'))
#       name  age state  point
# 0    Ellen   24    CA     88
# 1    Frank   30    NY     57
# 2  Charlie   18    CA     70
# 3    Alice   24    NY     64
# 4     Dave   68    TX     70
# 5      Bob   42    CA     92
