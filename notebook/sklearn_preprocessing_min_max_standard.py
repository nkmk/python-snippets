from sklearn import preprocessing

l = [0, 1, 2, 3, 4]
print(l)
# [0, 1, 2, 3, 4]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

mm = preprocessing.MinMaxScaler()

# mm.fit_transform(l)
# ValueError: Expected 2D array, got 1D array instead:

l_2d_min_max = mm.fit_transform(l_2d)

print(l_2d_min_max)
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(type(l_2d_min_max))
# <class 'numpy.ndarray'>

print(preprocessing.minmax_scale(l))
# [0.   0.25 0.5  0.75 1.  ]

print(preprocessing.minmax_scale(l_2d))
# [[0.  0.  0. ]
#  [0.5 0.5 0.5]
#  [1.  1.  1. ]]

print(preprocessing.minmax_scale(l_2d, axis=1))
# [[0.  0.5 1. ]
#  [0.  0.5 1. ]
#  [0.  0.5 1. ]]

ss = preprocessing.StandardScaler()

# print(ss.fit_transform(l))
# ValueError: Expected 2D array, got 1D array instead:

l_2d_standardization = ss.fit_transform(l_2d)

print(l_2d_standardization)
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(type(l_2d_standardization))
# <class 'numpy.ndarray'>

print(preprocessing.scale(l))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(preprocessing.scale(l_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(preprocessing.scale(l_2d, axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]
