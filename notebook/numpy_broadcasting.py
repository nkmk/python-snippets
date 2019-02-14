import numpy as np

a = np.zeros((3, 3), np.int)
print(a)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

print(a.shape)
# (3, 3)

b = np.arange(3)
print(b)
# [0 1 2]

print(b.shape)
# (3,)

print(a + b)
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

b_1_3 = b.reshape(1, 3)
print(b_1_3)
# [[0 1 2]]

print(b_1_3.shape)
# (1, 3)

print(np.tile(b_1_3, (3, 1)))
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

b_3_1 = b.reshape(3, 1)
print(b_3_1)
# [[0]
#  [1]
#  [2]]

print(b_3_1.shape)
# (3, 1)

print(a + b_3_1)
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]

print(np.tile(b_3_1, (1, 3)))
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]

print(b_1_3)
# [[0 1 2]]

print(b_1_3.shape)
# (1, 3)

print(b_3_1)
# [[0]
#  [1]
#  [2]]

print(b_3_1.shape)
# (3, 1)

print(b_1_3 + b_3_1)
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

print(np.tile(b_1_3, (3, 1)))
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

print(np.tile(b_3_1, (1, 3)))
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]

print(np.tile(b_1_3, (3, 1)) + np.tile(b_3_1, (1, 3)))
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

c = np.arange(4)
print(c)
# [0 1 2 3]

print(c.shape)
# (4,)

print(b_3_1)
# [[0]
#  [1]
#  [2]]

print(b_3_1.shape)
# (3, 1)

print(c + b_3_1)
# [[0 1 2 3]
#  [1 2 3 4]
#  [2 3 4 5]]

print(np.tile(c.reshape(1, 4), (3, 1)))
# [[0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]]

print(np.tile(b_3_1, (1, 4)))
# [[0 0 0 0]
#  [1 1 1 1]
#  [2 2 2 2]]

print(np.tile(c.reshape(1, 4), (3, 1)) + np.tile(b_3_1, (1, 4)))
# [[0 1 2 3]
#  [1 2 3 4]
#  [2 3 4 5]]
