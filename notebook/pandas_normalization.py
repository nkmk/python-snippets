import pandas as pd
import scipy.stats
from sklearn import preprocessing

print(pd.__version__)
# 2.1.4

print(scipy.__version__)
# 1.11.4

import sklearn  # Required only for version check

print(sklearn.__version__)
# 1.3.2

df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                  columns=['col1', 'col2', 'col3'],
                  index=['row1', 'row2', 'row3'])
print(df)
#       col1  col2  col3
# row1     0     1     2
# row2     3     4     5
# row3     6     7     8

s = df['col1']
print(s)
# row1    0
# row2    3
# row3    6
# Name: col1, dtype: int64

print(scipy.stats.zscore(df))
#           col1      col2      col3
# row1 -1.224745 -1.224745 -1.224745
# row2  0.000000  0.000000  0.000000
# row3  1.224745  1.224745  1.224745

print(scipy.stats.zscore(df, axis=1, ddof=1))
#       col1  col2  col3
# row1  -1.0   0.0   1.0
# row2  -1.0   0.0   1.0
# row3  -1.0   0.0   1.0

# print(scipy.stats.zscore(df, axis=None))
# ValueError: Unable to coerce to DataFrame, shape must be (3, 3): given (1, 1)

print(scipy.stats.zscore(df.values, axis=None))
# [[-1.54919334 -1.161895   -0.77459667]
#  [-0.38729833  0.          0.38729833]
#  [ 0.77459667  1.161895    1.54919334]]

print(pd.DataFrame(scipy.stats.zscore(df.values, axis=None),
                   index=df.index, columns=df.columns))
#           col1      col2      col3
# row1 -1.549193 -1.161895 -0.774597
# row2 -0.387298  0.000000  0.387298
# row3  0.774597  1.161895  1.549193

print(scipy.stats.zscore(s))
# row1   -1.224745
# row2    0.000000
# row3    1.224745
# Name: col1, dtype: float64

mm = preprocessing.MinMaxScaler()

print(mm.fit_transform(df))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.minmax_scale(df))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.scale(df))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(pd.DataFrame(preprocessing.minmax_scale(df, axis=1),
                   index=df.index, columns=df.columns))
#       col1  col2  col3
# row1   0.0   0.5   1.0
# row2   0.0   0.5   1.0
# row3   0.0   0.5   1.0

# print(mm.fit_transform(s))
# ValueError: Expected 2D array, got 1D array instead:

print(preprocessing.minmax_scale(s))
# [0.  0.5 1. ]

print(pd.Series(preprocessing.minmax_scale(s), index=s.index, name=s.name))
# row1    0.0
# row2    0.5
# row3    1.0
# Name: col1, dtype: float64

df_copy = df.copy()
df_copy['col1_min_max'] = preprocessing.minmax_scale(s)
df_copy['col1_standardization'] = preprocessing.scale(s)

print(df_copy)
#       col1  col2  col3  col1_min_max  col1_standardization
# row1     0     1     2           0.0             -1.224745
# row2     3     4     5           0.5              0.000000
# row3     6     7     8           1.0              1.224745

print((df - df.min()) / (df.max() - df.min()))
#       col1  col2  col3
# row1   0.0   0.0   0.0
# row2   0.5   0.5   0.5
# row3   1.0   1.0   1.0

print((df - df.mean()) / df.std())
#       col1  col2  col3
# row1  -1.0  -1.0  -1.0
# row2   0.0   0.0   0.0
# row3   1.0   1.0   1.0

print((df - df.mean()) / df.std(ddof=0))
#           col1      col2      col3
# row1 -1.224745 -1.224745 -1.224745
# row2  0.000000  0.000000  0.000000
# row3  1.224745  1.224745  1.224745

print(((df.T - df.T.min()) / (df.T.max() - df.T.min())).T)
#       col1  col2  col3
# row1   0.0   0.5   1.0
# row2   0.0   0.5   1.0
# row3   0.0   0.5   1.0

print(((df.T - df.T.mean()) / df.T.std()).T)
#       col1  col2  col3
# row1  -1.0   0.0   1.0
# row2  -1.0   0.0   1.0
# row3  -1.0   0.0   1.0

print(((df.T - df.T.mean()) / df.T.std(ddof=0)).T)
#           col1  col2      col3
# row1 -1.224745   0.0  1.224745
# row2 -1.224745   0.0  1.224745
# row3 -1.224745   0.0  1.224745

print((df - df.min(None)) / (df.max(None) - df.min(None)))
#        col1   col2   col3
# row1  0.000  0.125  0.250
# row2  0.375  0.500  0.625
# row3  0.750  0.875  1.000

print((df - df.mean(None)) / df.values.std())
#           col1      col2      col3
# row1 -1.549193 -1.161895 -0.774597
# row2 -0.387298  0.000000  0.387298
# row3  0.774597  1.161895  1.549193

print((df - df.mean(None)) / df.values.std(ddof=1))
#           col1      col2      col3
# row1 -1.460593 -1.095445 -0.730297
# row2 -0.365148  0.000000  0.365148
# row3  0.730297  1.095445  1.460593

print((s - s.min()) / (s.max() - s.min()))
# row1    0.0
# row2    0.5
# row3    1.0
# Name: col1, dtype: float64

print((s - s.mean()) / s.std())
# row1   -1.0
# row2    0.0
# row3    1.0
# Name: col1, dtype: float64

print((s - s.mean()) / s.std(ddof=0))
# row1   -1.224745
# row2    0.000000
# row3    1.224745
# Name: col1, dtype: float64
