import pandas as pd
import scipy.stats
from sklearn import preprocessing

df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                  columns=['col1', 'col2', 'col3'],
                  index=['a', 'b', 'c'])

print(df)
#    col1  col2  col3
# a     0     1     2
# b     3     4     5
# c     6     7     8

print((df - df.min()) / (df.max() - df.min()))
#    col1  col2  col3
# a   0.0   0.0   0.0
# b   0.5   0.5   0.5
# c   1.0   1.0   1.0

print(((df.T - df.T.min()) / (df.T.max() - df.T.min())).T)
#    col1  col2  col3
# a   0.0   0.5   1.0
# b   0.0   0.5   1.0
# c   0.0   0.5   1.0

print((df - df.values.min()) / (df.values.max() - df.values.min()))
#     col1   col2   col3
# a  0.000  0.125  0.250
# b  0.375  0.500  0.625
# c  0.750  0.875  1.000

print((df - df.mean()) / df.std())
#    col1  col2  col3
# a  -1.0  -1.0  -1.0
# b   0.0   0.0   0.0
# c   1.0   1.0   1.0

print((df - df.mean()) / df.std(ddof=0))
#        col1      col2      col3
# a -1.224745 -1.224745 -1.224745
# b  0.000000  0.000000  0.000000
# c  1.224745  1.224745  1.224745

print(((df.T - df.T.mean()) / df.T.std()).T)
#    col1  col2  col3
# a  -1.0   0.0   1.0
# b  -1.0   0.0   1.0
# c  -1.0   0.0   1.0

print(((df.T - df.T.mean()) / df.T.std(ddof=0)).T)
#        col1  col2      col3
# a -1.224745   0.0  1.224745
# b -1.224745   0.0  1.224745
# c -1.224745   0.0  1.224745

print((df - df.values.mean()) / df.values.std())
#        col1      col2      col3
# a -1.549193 -1.161895 -0.774597
# b -0.387298  0.000000  0.387298
# c  0.774597  1.161895  1.549193

print((df - df.values.mean()) / df.values.std(ddof=1))
#        col1      col2      col3
# a -1.460593 -1.095445 -0.730297
# b -0.365148  0.000000  0.365148
# c  0.730297  1.095445  1.460593

df_ = df.copy()
s = df_['col1']
df_['col1_min_max'] = (s - s.min()) / (s.max() - s.min())
df_['col1_standardization'] = (s - s.mean()) / s.std()

print(df_)
#    col1  col2  col3  col1_min_max  col1_standardization
# a     0     1     2           0.0                  -1.0
# b     3     4     5           0.5                   0.0
# c     6     7     8           1.0                   1.0

print(scipy.stats.zscore(df))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(type(scipy.stats.zscore(df)))
# <class 'numpy.ndarray'>

print(scipy.stats.zscore(df, axis=None, ddof=1))
# [[-1.46059349 -1.09544512 -0.73029674]
#  [-0.36514837  0.          0.36514837]
#  [ 0.73029674  1.09544512  1.46059349]]

df_standardization = pd.DataFrame(scipy.stats.zscore(df),
                                  index=df.index, columns=df.columns)

print(df_standardization)
#        col1      col2      col3
# a -1.224745 -1.224745 -1.224745
# b  0.000000  0.000000  0.000000
# c  1.224745  1.224745  1.224745

df_ = df.copy()
df_['col1_standardization'] = scipy.stats.zscore(df_['col1'])
print(df_)
#    col1  col2  col3  col1_standardization
# a     0     1     2             -1.224745
# b     3     4     5              0.000000
# c     6     7     8              1.224745

mm = preprocessing.MinMaxScaler()

print(mm.fit_transform(df))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(type(mm.fit_transform(df)))
# <class 'numpy.ndarray'>

print(preprocessing.minmax_scale(df))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(type(preprocessing.minmax_scale(df)))
# <class 'numpy.ndarray'>

df_min_max = pd.DataFrame(mm.fit_transform(df),
                          index=df.index, columns=df.columns)

print(df_min_max)
#    col1  col2  col3
# a   0.0   0.0   0.0
# b   0.5   0.5   0.5
# c   1.0   1.0   1.0

df_ = df.copy()
s = df_['col1'].astype(float)
df_['col1_min_max'] = preprocessing.minmax_scale(s)
df_['col1_standardization'] = preprocessing.scale(s)

print(df_)
#    col1  col2  col3  col1_min_max  col1_standardization
# a     0     1     2           0.0             -1.224745
# b     3     4     5           0.5              0.000000
# c     6     7     8           1.0              1.224745
