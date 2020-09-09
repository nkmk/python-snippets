import numpy as np

print(np.__version__)
# 1.19.0

a_1d = np.array([1, 2, 3, 4, 5, 6])
print(a_1d)
# [1 2 3 4 5 6]

print(np.cumsum(a_1d))
# [ 1  3  6 10 15 21]

print(np.cumsum(a_1d, dtype=float))
# [ 1.  3.  6. 10. 15. 21.]

print(a_1d.cumsum())
# [ 1  3  6 10 15 21]

print(a_1d.cumsum(dtype=float))
# [ 1.  3.  6. 10. 15. 21.]

l = [1, 2, 3, 4, 5, 6]

print(np.cumsum(l))
# [ 1  3  6 10 15 21]

print(type(np.cumsum(l)))
# <class 'numpy.ndarray'>

a_2d = a_1d.reshape(2, 3)
print(a_2d)
# [[1 2 3]
#  [4 5 6]]

print(np.cumsum(a_2d))
# [ 1  3  6 10 15 21]

print(np.cumsum(a_2d, axis=0))
# [[1 2 3]
#  [5 7 9]]

print(np.cumsum(a_2d, axis=1))
# [[ 1  3  6]
#  [ 4  9 15]]

print(a_2d.cumsum())
# [ 1  3  6 10 15 21]

print(a_2d.cumsum(axis=0))
# [[1 2 3]
#  [5 7 9]]

print(a_2d.cumsum(axis=1))
# [[ 1  3  6]
#  [ 4  9 15]]

l_2d = [[1, 2, 3], [4, 5, 6]]

print(np.cumsum(l_2d))
# [ 1  3  6 10 15 21]

print(np.cumsum(l_2d, axis=0))
# [[1 2 3]
#  [5 7 9]]

print(np.cumsum(l_2d, axis=1))
# [[ 1  3  6]
#  [ 4  9 15]]

l_2d_error = [[1, 2, 3], [4, 5]]

print(np.cumsum(l_2d_error))
# [list([1, 2, 3]) list([1, 2, 3, 4, 5])]
# 
# /usr/local/lib/python3.8/site-packages/numpy/core/_asarray.py:83: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
#   return array(a, dtype, copy=False, order=order)

print(np.cumprod(a_1d))
# [  1   2   6  24 120 720]

print(np.cumprod(a_1d, dtype=float))
# [  1.   2.   6.  24. 120. 720.]

print(a_1d.cumprod())
# [  1   2   6  24 120 720]

print(a_1d.cumprod(dtype=float))
# [  1.   2.   6.  24. 120. 720.]

print(np.cumprod(a_2d))
# [  1   2   6  24 120 720]

print(np.cumprod(a_2d, axis=0))
# [[ 1  2  3]
#  [ 4 10 18]]

print(np.cumprod(a_2d, axis=1))
# [[  1   2   6]
#  [  4  20 120]]

print(a_2d.cumprod())
# [  1   2   6  24 120 720]

print(a_2d.cumprod(axis=0))
# [[ 1  2  3]
#  [ 4 10 18]]

print(a_2d.cumprod(axis=1))
# [[  1   2   6]
#  [  4  20 120]]

print(np.cumprod(l))
# [  1   2   6  24 120 720]

print(np.cumprod(l_2d))
# [  1   2   6  24 120 720]

print(np.cumprod(l_2d, axis=0))
# [[ 1  2  3]
#  [ 4 10 18]]

print(np.cumprod(l_2d, axis=1))
# [[  1   2   6]
#  [  4  20 120]]
