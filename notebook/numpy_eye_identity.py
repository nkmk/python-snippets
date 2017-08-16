import numpy as np

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html

e = np.eye(4)
print(type(e))
print(e)
print(e.dtype)
# <class 'numpy.ndarray'>
# [[ 1.  0.  0.  0.]
#  [ 0.  1.  0.  0.]
#  [ 0.  0.  1.  0.]
#  [ 0.  0.  0.  1.]]
# float64

e = np.eye(4, M=3, k=1, dtype=np.int8)
print(e)
print(e.dtype)
# [[0 1 0]
#  [0 0 1]
#  [0 0 0]
#  [0 0 0]]
# int8

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html

i = np.identity(4)
print(i)
print(i.dtype)
# [[ 1.  0.  0.  0.]
#  [ 0.  1.  0.  0.]
#  [ 0.  0.  1.  0.]
#  [ 0.  0.  0.  1.]]
# float64

i = np.identity(4, dtype=np.uint8)
print(i)
print(i.dtype)
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]
# uint8

a = [3, 0, 8, 1, 9]
a_one_hot = np.identity(10)[a]
print(a)
print(a_one_hot)
# [3, 0, 8, 1, 9]
# [[ 0.  0.  0.  1.  0.  0.  0.  0.  0.  0.]
#  [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]]

a = [2, 2, 0, 1, 0]
a_one_hot = np.identity(3)[a]
print(a)
print(a_one_hot)
# [2, 2, 0, 1, 0]
# [[ 0.  0.  1.]
#  [ 0.  0.  1.]
#  [ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 1.  0.  0.]]
