import pandas as pd
import numpy as np

df = pd.read_csv('data/src/sample_pandas_normal.csv')
df.iloc[1] = np.nan
print(df)
#       name   age state  point
# 0    Alice  24.0    NY   64.0
# 1      NaN   NaN   NaN    NaN
# 2  Charlie  18.0    CA   70.0
# 3     Dave  68.0    TX   70.0
# 4    Ellen  24.0    CA   88.0
# 5    Frank  30.0    NY   57.0

u = df['state'].unique()
print(u)
print(type(u))
# ['NY' nan 'CA' 'TX']
# <class 'numpy.ndarray'>

vc = df['state'].value_counts()
print(vc)
print(type(vc))
# NY    2
# CA    2
# TX    1
# Name: state, dtype: int64
# <class 'pandas.core.series.Series'>

print(df['state'].value_counts(ascending=True))
# TX    1
# CA    2
# NY    2
# Name: state, dtype: int64

print(df['state'].value_counts(sort=False))
# CA    2
# NY    2
# TX    1
# Name: state, dtype: int64

print(df['state'].value_counts(dropna=False))
# NY     2
# CA     2
# TX     1
# NaN    1
# Name: state, dtype: int64

print(df['state'].value_counts(dropna=False, normalize=True))
# NY     0.333333
# CA     0.333333
# TX     0.166667
# NaN    0.166667
# Name: state, dtype: float64

nu = df['state'].nunique()
print(nu)
print(type(nu))
# 3
# <class 'int'>

print(df['state'].nunique(dropna=False))
# 4

nu_col = df.nunique()
print(nu_col)
print(type(nu_col))
# name     5
# age      4
# state    3
# point    4
# dtype: int64
# <class 'pandas.core.series.Series'>

print(df.nunique(dropna=False))
# name     6
# age      5
# state    4
# point    5
# dtype: int64

print(df.nunique(dropna=False, axis='columns'))
# 0    4
# 1    1
# 2    4
# 3    4
# 4    4
# 5    4
# dtype: int64

print(df['state'].nunique())
# 3

print(df.nunique())
# name     5
# age      4
# state    3
# point    4
# dtype: int64

print(df['state'].unique().tolist())
print(type(df['state'].unique().tolist()))
# ['NY', nan, 'CA', 'TX']
# <class 'list'>

print(df['state'].value_counts().index.tolist())
print(type(df['state'].value_counts().index.tolist()))
# ['NY', 'CA', 'TX']
# <class 'list'>

print(df['state'].value_counts(dropna=False).index.values)
print(type(df['state'].value_counts().index.values))
# ['NY' 'CA' 'TX' nan]
# <class 'numpy.ndarray'>

print(df['state'].value_counts()['NY'])
# 2

print(df['state'].value_counts().NY)
# 2

for index, value in df['state'].value_counts().iteritems():
    print(index, ': ', value)
# NY :  2
# CA :  2
# TX :  1

d = df['state'].value_counts().to_dict()
print(d)
print(type(d))
# {'NY': 2, 'CA': 2, 'TX': 1}
# <class 'dict'>

print(d['NY'])
# 2

for key, value in d.items():
    print(key, ': ', value)
# NY :  2
# CA :  2
# TX :  1

print(df['state'].value_counts())
# NY    2
# CA    2
# TX    1
# Name: state, dtype: int64

print(df['state'].value_counts().index[0])
# NY

print(df['state'].value_counts().iat[0])
# 2

print(df.apply(lambda x: x.value_counts().index[0]))
# name     Frank
# age         24
# state       NY
# point       70
# dtype: object

print(df.apply(lambda x: x.value_counts().iat[0]))
# name     1
# age      2
# state    2
# point    2
# dtype: int64

print(df['state'].mode())
# 0    CA
# 1    NY
# dtype: object

print(df['state'].mode().tolist())
# ['CA', 'NY']

print(df['age'].mode().tolist())
# [24.0]

s_mode = df.apply(lambda x: x.mode().tolist())
print(s_mode)
# name     [Alice, Charlie, Dave, Ellen, Frank]
# age                                    [24.0]
# state                                [CA, NY]
# point                                  [70.0]
# dtype: object

print(type(s_mode))
# <class 'pandas.core.series.Series'>

print(s_mode['name'])
# ['Alice', 'Charlie', 'Dave', 'Ellen', 'Frank']

print(type(s_mode['name']))
# <class 'list'>

print(df.mode())
#       name   age state  point
# 0    Alice  24.0    CA   70.0
# 1  Charlie   NaN    NY    NaN
# 2     Dave   NaN   NaN    NaN
# 3    Ellen   NaN   NaN    NaN
# 4    Frank   NaN   NaN    NaN

print(df.mode().count())
# name     5
# age      1
# state    2
# point    1
# dtype: int64

print(df.astype('str').describe())
#          name   age state point
# count       6     6     6     6
# unique      6     5     4     5
# top     Frank  24.0    CA  70.0
# freq        1     2     2     2

print(df.astype('str').describe().loc['top'])
# name     Frank
# age       24.0
# state       CA
# point     70.0
# Name: top, dtype: object
