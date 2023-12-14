import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.read_csv('data/src/sample_pandas_normal.csv')
df.iloc[1] = float('nan')
print(df)
#       name   age state  point
# 0    Alice  24.0    NY   64.0
# 1      NaN   NaN   NaN    NaN
# 2  Charlie  18.0    CA   70.0
# 3     Dave  68.0    TX   70.0
# 4    Ellen  24.0    CA   88.0
# 5    Frank  30.0    NY   57.0

print(df['state'].unique())
# ['NY' nan 'CA' 'TX']

print(type(df['state'].unique()))
# <class 'numpy.ndarray'>

print(df['state'].value_counts())
# state
# NY    2
# CA    2
# TX    1
# Name: count, dtype: int64

print(type(df['state'].value_counts()))
# <class 'pandas.core.series.Series'>

print(df['state'].value_counts(dropna=False))
# state
# NY     2
# CA     2
# NaN    1
# TX     1
# Name: count, dtype: int64

print(df['state'].value_counts(dropna=False, ascending=True))
# state
# NaN    1
# TX     1
# NY     2
# CA     2
# Name: count, dtype: int64

print(df['state'].value_counts(dropna=False, sort=False))
# state
# NY     2
# NaN    1
# CA     2
# TX     1
# Name: count, dtype: int64

print(df['state'].value_counts(normalize=True))
# state
# NY    0.4
# CA    0.4
# TX    0.2
# Name: proportion, dtype: float64

print(df['state'].value_counts(dropna=False, normalize=True))
# state
# NY     0.333333
# CA     0.333333
# NaN    0.166667
# TX     0.166667
# Name: proportion, dtype: float64

print(df['state'].nunique())
# 3

print(type(df['state'].nunique()))
# <class 'int'>

print(df['state'].nunique(dropna=False))
# 4

print(df.nunique())
# name     5
# age      4
# state    3
# point    4
# dtype: int64

print(type(df.nunique()))
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
# ['NY', nan, 'CA', 'TX']

print(type(df['state'].unique().tolist()))
# <class 'list'>

print(df['state'].value_counts().index.tolist())
# ['NY', 'CA', 'TX']

print(type(df['state'].value_counts().index.tolist()))
# <class 'list'>

print(df['state'].value_counts().index.values)
# ['NY' 'CA' 'TX']

print(type(df['state'].value_counts().index.values))
# <class 'numpy.ndarray'>

print(df['state'].value_counts(dropna=False).index.tolist())
# ['NY', 'CA', nan, 'TX']

vc = df['state'].value_counts()
print(vc)
# state
# NY    2
# CA    2
# TX    1
# Name: count, dtype: int64

print(vc['NY'])
# 2

print(vc['TX'])
# 1

for index, value in df['state'].value_counts().items():
    print(index, value)
# NY 2
# CA 2
# TX 1

d = df['state'].value_counts().to_dict()
print(d)
# {'NY': 2, 'CA': 2, 'TX': 1}

print(type(d))
# <class 'dict'>

print(d['NY'])
# 2

print(d['TX'])
# 1

for key, value in d.items():
    print(key, value)
# NY 2
# CA 2
# TX 1

print(df['state'].value_counts())
# state
# NY    2
# CA    2
# TX    1
# Name: count, dtype: int64

print(df['state'].value_counts().index[0])
# NY

print(df['state'].value_counts().iat[0])
# 2

# print(df['age'].value_counts()[0])
# KeyError: 0

print(df['age'].value_counts().iat[0])
# 2

print(df.apply(lambda x: x.value_counts().index[0]))
# name     Alice
# age       24.0
# state       NY
# point     70.0
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
# Name: state, dtype: object

print(df['state'].mode().tolist())
# ['CA', 'NY']

print(df['age'].mode().tolist())
# [24.0]

s_list = df.apply(lambda x: x.mode().tolist())
print(s_list)
# name     [Alice, Charlie, Dave, Ellen, Frank]
# age                                    [24.0]
# state                                [CA, NY]
# point                                  [70.0]
# dtype: object

print(type(s_list))
# <class 'pandas.core.series.Series'>

print(s_list['name'])
# ['Alice', 'Charlie', 'Dave', 'Ellen', 'Frank']

print(type(s_list['name']))
# <class 'list'>

print(df.mode())
#       name   age state  point
# 0    Alice  24.0    CA   70.0
# 1  Charlie   NaN    NY    NaN
# 2     Dave   NaN   NaN    NaN
# 3    Ellen   NaN   NaN    NaN
# 4    Frank   NaN   NaN    NaN

print(df.astype('object').describe())
#          name   age state  point
# count       5   5.0     5    5.0
# unique      5   4.0     3    4.0
# top     Alice  24.0    NY   70.0
# freq        1   2.0     2    2.0

print(df.astype('object').describe().loc['top'])
# name     Alice
# age       24.0
# state       NY
# point     70.0
# Name: top, dtype: object
