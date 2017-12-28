import numpy as np

a_int = np.arange(6).reshape((2,3))
print(a_int)
# [[0 1 2]
#  [3 4 5]]

a_float = np.arange(6).reshape((2,3)) / 10
print(a_float)
# [[ 0.   0.1  0.2]
#  [ 0.3  0.4  0.5]]

print(np.zeros_like(a_int))
# [[0 0 0]
#  [0 0 0]]

print(np.zeros_like(a_float))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

print(np.zeros_like(a_int, dtype=np.float))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

print(np.ones_like(a_int))
# [[1 1 1]
#  [1 1 1]]

print(np.ones_like(a_float))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

print(np.ones_like(a_int, dtype=np.float))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

print(np.full_like(a_int, 100))
# [[100 100 100]
#  [100 100 100]]

print(np.full_like(a_float, 100))
# [[ 100.  100.  100.]
#  [ 100.  100.  100.]]

print(np.full_like(a_int, 0.123))
# [[0 0 0]
#  [0 0 0]]

print(np.full_like(a_float, 0.123))
# [[ 0.123  0.123  0.123]
#  [ 0.123  0.123  0.123]]

print(np.full_like(a_int, 0.123, dtype=np.float))
# [[ 0.123  0.123  0.123]
#  [ 0.123  0.123  0.123]]
