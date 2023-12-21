import sklearn  # Required only for version check

print(sklearn.__version__)
# 1.3.2

from sklearn import preprocessing

l_1d = [0, 1, 2, 3, 4]
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

mm = preprocessing.MinMaxScaler()

# mm.fit_transform(l_1d)
# ValueError: Expected 2D array, got 1D array instead:

print(mm.fit_transform(l_2d))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(type(mm.fit_transform(l_2d)))
# <class 'numpy.ndarray'>

print(preprocessing.minmax_scale(l_1d))
# [0.   0.25 0.5  0.75 1.  ]

print(preprocessing.minmax_scale(l_2d))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.minmax_scale(l_2d, axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

# print(preprocessing.minmax_scale(l_2d, axis=None))
# InvalidParameterError: The 'axis' parameter of minmax_scale must be a int among {0, 1}. Got None instead.

ss = preprocessing.StandardScaler()

print(ss.fit_transform(l_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(type(ss.fit_transform(l_2d)))
# <class 'numpy.ndarray'>

print(preprocessing.scale(l_1d))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(preprocessing.scale(l_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(preprocessing.scale(l_2d, axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]
