import numpy as np

a = np.zeros((4, 3), dtype=np.int)
print(a)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]
#  [0 0 0]]

print(a.shape)
# (4, 3)

b = np.arange(6).reshape(2, 3)
print(b)
# [[0 1 2]
#  [3 4 5]]

print(b.shape)
# (2, 3)

# print(a + b)
# ValueError: operands could not be broadcast together with shapes (4,3) (2,3) 

a = np.zeros((2, 3, 4), dtype=np.int)
print(a)
# [[[0 0 0 0]
#   [0 0 0 0]
#   [0 0 0 0]]
# 
#  [[0 0 0 0]
#   [0 0 0 0]
#   [0 0 0 0]]]

print(a.shape)
# (2, 3, 4)

b = np.arange(3)
print(b)
# [0 1 2]

print(b.shape)
# (3,)

# print(a + b)
# ValueError: operands could not be broadcast together with shapes (2,3,4) (3,) 

b_3_1 = b.reshape(3, 1)
print(b_3_1)
# [[0]
#  [1]
#  [2]]

print(b_3_1.shape)
# (3, 1)

print(a + b_3_1)
# [[[0 0 0 0]
#   [1 1 1 1]
#   [2 2 2 2]]
# 
#  [[0 0 0 0]
#   [1 1 1 1]
#   [2 2 2 2]]]
