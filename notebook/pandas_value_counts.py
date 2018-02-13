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

u = df['state'].unique()
print(u)
print(type(u))
# ['NY' 'CA' 'TX']
# <class 'numpy.ndarray'>

vc = df['state'].value_counts()
print(vc)
print(type(vc))
# CA    3
# NY    2
# TX    1
# Name: state, dtype: int64
# <class 'pandas.core.series.Series'>

vc_f = df['state'].value_counts(sort=False)
print(vc_f)
# TX    1
# CA    3
# NY    2
# Name: state, dtype: int64

print(len(u))
# 3

print(len(vc))
# 3

print(vc.count())
# 3

print(u.tolist())
print(type(u.tolist()))
# ['NY', 'CA', 'TX']
# <class 'list'>

print(vc.index.tolist())
print(type(vc.index.tolist()))
# ['CA', 'NY', 'TX']
# <class 'list'>

print(vc.index.values)
print(type(vc.index.values))
# ['CA' 'NY' 'TX']
# <class 'numpy.ndarray'>

print(vc['NY'])
# 2

print(vc.NY)
# 2

for index, value in vc.iteritems():
    print(index, ': ', value)
# CA :  3
# NY :  2
# TX :  1

d = vc.to_dict()
print(d)
print(type(d))
# {'CA': 3, 'NY': 2, 'TX': 1}
# <class 'dict'>

print(d['NY'])
# 2

for key, value in d.items():
    print(key, ': ', value)
# CA :  3
# NY :  2
# TX :  1

vc_norm = df['state'].value_counts(normalize=True)
print(vc_norm)
# CA    0.500000
# NY    0.333333
# TX    0.166667
# Name: state, dtype: float64
