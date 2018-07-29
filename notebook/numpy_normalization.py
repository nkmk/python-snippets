import numpy as np
import scipy.stats
from sklearn import preprocessing

a = np.array([0, 1, 2, 3, 4])
print(a)
# [0 1 2 3 4]

print((a - a.min()) / (a.max() - a.min()))
# [0.   0.25 0.5  0.75 1.  ]

print((a - a.mean()) / a.std())
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print((a - a.mean()) / a.std(ddof=1))
# [-1.26491106 -0.63245553  0.          0.63245553  1.26491106]

a_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(a_2d)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

def min_max(x, axis=None):
    x_min = x.min(axis=axis, keepdims=True)
    x_max = x.max(axis=axis, keepdims=True)
    return (x - x_min) / (x_max - x_min)

print(min_max(a_2d))
# [[0.    0.125 0.25 ]
#  [0.375 0.5   0.625]
#  [0.75  0.875 1.   ]]

print(min_max(a_2d, axis=0))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(min_max(a_2d, axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

print(min_max(a))
# [0.   0.25 0.5  0.75 1.  ]

def standardization(x, axis=None, ddof=0):
    x_mean = x.mean(axis=axis, keepdims=True)
    x_std = x.std(axis=axis, keepdims=True, ddof=ddof)
    return (x - x_mean) / x_std

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

print(standardization(a))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(standardization(a, ddof=1))
# [-1.26491106 -0.63245553  0.          0.63245553  1.26491106]

print(scipy.stats.zscore(a))
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

print(mm.fit_transform(a_2d.astype(float)))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.minmax_scale(a.astype(float)))
# [0.   0.25 0.5  0.75 1.  ]

print(preprocessing.minmax_scale(a_2d.astype(float), axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

ss = preprocessing.StandardScaler()

print(ss.fit_transform(a_2d.astype(float)))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(preprocessing.scale(a.astype(float)))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(preprocessing.scale(a_2d.astype(float), axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]
