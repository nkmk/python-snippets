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

s = df['state'].value_counts()
print(s)
# CA    3
# NY    2
# TX    1
# Name: state, dtype: int64

print(type(s))
# <class 'pandas.core.series.Series'>

print(len(s))
# 3

print(s.count())
# 3

print(s.index.tolist())
# ['CA', 'NY', 'TX']

print(s['NY'])
# 2

print(s.NY)
# 2

d = s.to_dict()
print(d)
# {'CA': 3, 'NY': 2, 'TX': 1}

print(d['NY'])
# 2

s_norm = df['state'].value_counts(normalize=True)
print(s_norm)
# CA    0.500000
# NY    0.333333
# TX    0.166667
# Name: state, dtype: float64

print(s_norm.sum())
# 1.0
