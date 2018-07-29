import scipy.stats

l = [0, 1, 2, 3, 4]
print(l)
# [0, 1, 2, 3, 4]

print(scipy.stats.zscore(l))
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]

print(type(scipy.stats.zscore(l)))
# <class 'numpy.ndarray'>

print(scipy.stats.zscore(l, ddof=1))
# [-1.26491106 -0.63245553  0.          0.63245553  1.26491106]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(scipy.stats.zscore(l_2d))
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]

print(scipy.stats.zscore(l_2d, ddof=1))
# [[-1. -1. -1.]
#  [ 0.  0.  0.]
#  [ 1.  1.  1.]]

print(scipy.stats.zscore(l_2d, axis=1))
# [[-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]
#  [-1.22474487  0.          1.22474487]]

print(scipy.stats.zscore(l_2d, axis=1, ddof=1))
# [[-1.  0.  1.]
#  [-1.  0.  1.]
#  [-1.  0.  1.]]

print(scipy.stats.zscore(l_2d, axis=None))
# [[-1.54919334 -1.161895   -0.77459667]
#  [-0.38729833  0.          0.38729833]
#  [ 0.77459667  1.161895    1.54919334]]

print(scipy.stats.zscore(l_2d, axis=None, ddof=1))
# [[-1.46059349 -1.09544512 -0.73029674]
#  [-0.36514837  0.          0.36514837]
#  [ 0.73029674  1.09544512  1.46059349]]
