import numpy as np
import scipy.stats
from sklearn import preprocessing

print(np.__version__)
# 1.26.2

print(scipy.__version__)
# 1.11.4

import sklearn  # Required only for version check

print(sklearn.__version__)
# 1.3.2

a_1d = np.array([0, 1, 2, 3, 4])
print(a_1d)
# [0 1 2 3 4]

a_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(a_2d)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(scipy.stats.zscore(a_1d))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(scipy.stats.zscore(a_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(scipy.stats.zscore(a_2d, axis=None, ddof=1))
# [[-1.46059349 -1.09544512 -0.73029674]
#  [-0.36514837  0.          0.36514837]
#  [ 0.73029674  1.09544512  1.46059349]]

mm = preprocessing.MinMaxScaler()

print(mm.fit_transform(a_2d))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.minmax_scale(a_1d))
# [0.   0.25 0.5  0.75 1.  ]

print(preprocessing.minmax_scale(a_2d, axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

ss = preprocessing.StandardScaler()

print(ss.fit_transform(a_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(preprocessing.scale(a_1d))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(preprocessing.scale(a_2d, axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]

def min_max_normalization(a, axis=None):
    a_min = a.min(axis=axis, keepdims=True)
    a_max = a.max(axis=axis, keepdims=True)
    return (a - a_min) / (a_max - a_min)

print(min_max_normalization(a_1d))
# [0.   0.25 0.5  0.75 1.  ]

print(min_max_normalization(a_2d))
# [[0.    0.125 0.25 ]
#  [0.375 0.5   0.625]
#  [0.75  0.875 1.   ]]

print(min_max_normalization(a_2d, axis=0))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(min_max_normalization(a_2d, axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

def standardization(a, axis=None, ddof=0):
    a_mean = a.mean(axis=axis, keepdims=True)
    a_std = a.std(axis=axis, keepdims=True, ddof=ddof)
    return (a - a_mean) / a_std

print(standardization(a_1d))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(standardization(a_1d, ddof=1))
# [-1.26491106 -0.63245553  0.          0.63245553  1.26491106]

print(standardization(a_2d))
# [[-1.54919334 -1.161895   -0.77459667]
#  [-0.38729833  0.          0.38729833]
#  [ 0.77459667  1.161895    1.54919334]]

print(standardization(a_2d, ddof=1))
# [[-1.46059349 -1.09544512 -0.73029674]
#  [-0.36514837  0.          0.36514837]
#  [ 0.73029674  1.09544512  1.46059349]]

print(standardization(a_2d, axis=0))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(standardization(a_2d, axis=0, ddof=1))
# [[-1. -1. -1.]
#  [ 0.  0.  0.]
#  [ 1.  1.  1.]]

print(standardization(a_2d, axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]

print(standardization(a_2d, axis=1, ddof=1))
# [[-1.  0.  1.]
#  [-1.  0.  1.]
#  [-1.  0.  1.]]
