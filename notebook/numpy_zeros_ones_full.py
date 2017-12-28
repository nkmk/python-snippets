import numpy as np

print(np.zeros(3))
# [ 0.  0.  0.]

print(np.zeros((2, 3)))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

print(np.zeros(3).dtype)
# float64

print(np.zeros(3, dtype=np.int))
# [0 0 0]

print(np.zeros(3, dtype=np.int).dtype)
# int64

print(np.ones(3))
# [ 1.  1.  1.]

print(np.ones((2, 3)))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

print(np.ones(3).dtype)
# float64

print(np.ones(3, dtype=np.int))
# [1 1 1]

print(np.ones(3, dtype=np.int).dtype)
# int64

print(np.full(3, 100))
# [100 100 100]

print(np.full(3, np.pi))
# [ 3.14159265  3.14159265  3.14159265]

print(np.full((2, 3), 100))
# [[100 100 100]
#  [100 100 100]]

print(np.full((2, 3), np.pi))
# [[ 3.14159265  3.14159265  3.14159265]
#  [ 3.14159265  3.14159265  3.14159265]]

print(np.full(3, 100).dtype)
# int64

print(np.full(3, 100.0).dtype)
# float64

print(np.full(3, np.pi).dtype)
# float64

print(np.full(3, 100, dtype=float))
# [ 100.  100.  100.]

print(np.full(3, np.pi, dtype=int))
# [3 3 3]
