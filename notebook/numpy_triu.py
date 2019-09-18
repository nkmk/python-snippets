import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

print(np.triu(a))
# [[ 0  1  2  3]
#  [ 0  5  6  7]
#  [ 0  0 10 11]
#  [ 0  0  0 15]]

print(np.triu(a, k=2))
# [[0 0 2 3]
#  [0 0 0 7]
#  [0 0 0 0]
#  [0 0 0 0]]

print(np.triu(a, k=-1))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 0  9 10 11]
#  [ 0  0 14 15]]

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.triu(a))
# [[ 0  1  2  3]
#  [ 0  5  6  7]
#  [ 0  0 10 11]]

print(np.triu(a, k=-1))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 0  9 10 11]]

print(np.triu(np.arange(16).reshape(1, 1, 4, 4)))
# [[[[ 0  1  2  3]
#    [ 0  5  6  7]
#    [ 0  0 10 11]
#    [ 0  0  0 15]]]]
