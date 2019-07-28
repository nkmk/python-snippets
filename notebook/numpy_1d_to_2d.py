import numpy as np

a = np.arange(6)
print(a)
# [0 1 2 3 4 5]

print(a.reshape(2, 3))
# [[0 1 2]
#  [3 4 5]]

print(a.reshape(-1, 3))
# [[0 1 2]
#  [3 4 5]]

print(a.reshape(2, -1))
# [[0 1 2]
#  [3 4 5]]

# print(a.reshape(3, 4))
# ValueError: cannot reshape array of size 6 into shape (3,4)

# print(a.reshape(-1, 4))
# ValueError: cannot reshape array of size 6 into shape (4)

l = [0, 1, 2, 3, 4, 5]

print(np.array(l).reshape(-1, 3).tolist())
# [[0, 1, 2], [3, 4, 5]]

print(np.array(l).reshape(3, -1).tolist())
# [[0, 1], [2, 3], [4, 5]]
