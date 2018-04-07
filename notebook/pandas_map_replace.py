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

s = df['state']
print(s)
# 0    NY
# 1    CA
# 2    CA
# 3    TX
# 4    CA
# 5    NY
# Name: state, dtype: object

s_map_all = s.map({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'})
print(s_map_all)
# 0       NewYork
# 1    California
# 2    California
# 3         Texas
# 4    California
# 5       NewYork
# Name: state, dtype: object

s_replace_all = s.replace({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'})
print(s_replace_all)
# 0       NewYork
# 1    California
# 2    California
# 3         Texas
# 4    California
# 5       NewYork
# Name: state, dtype: object

s_map = s.map({'NY': 'NewYork'})
print(s_map)
# 0    NewYork
# 1        NaN
# 2        NaN
# 3        NaN
# 4        NaN
# 5    NewYork
# Name: state, dtype: object

s_replace = s.replace({'NY': 'NewYork'})
print(s_replace)
# 0    NewYork
# 1         CA
# 2         CA
# 3         TX
# 4         CA
# 5    NewYork
# Name: state, dtype: object

s_copy = s.copy()
s_copy.update(s_copy.map({'NY': 'NewYork'}))
print(s_copy)
# 0    NewYork
# 1         CA
# 2         CA
# 3         TX
# 4         CA
# 5    NewYork
# Name: state, dtype: object

s_copy = s.copy()
s_copy.replace({'NY': 'NewYork'}, inplace=True)
print(s_copy)
# 0    NewYork
# 1         CA
# 2         CA
# 3         TX
# 4         CA
# 5    NewYork
# Name: state, dtype: object

s_map_num = s.map({'NY': 0, 'CA': 1, 'TX': 2})
print(s_map_num)
# 0    0
# 1    1
# 2    1
# 3    2
# 4    1
# 5    0
# Name: state, dtype: int64

df['state'] = df['state'].map({'NY': 0, 'CA': 1, 'TX': 2})
print(df)
#       name  age  state  point
# 0    Alice   24      0     64
# 1      Bob   42      1     92
# 2  Charlie   18      1     70
# 3     Dave   68      2     70
# 4    Ellen   24      1     88
# 5    Frank   30      0     57

print(df['state'].dtype)
# int64
