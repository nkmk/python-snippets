import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

b = np.zeros_like(a)
print(b)
# [[0 0 0]
#  [0 0 0]]

print(a)
# [[0 1 2]
#  [3 4 5]]

a[:, :] = 0
print(a)
# [[0 0 0]
#  [0 0 0]]

a[:] = 1
print(a)
# [[1 1 1]
#  [1 1 1]]

a[:] = 0.1
print(a)
# [[0 0 0]
#  [0 0 0]]

a = a.astype(np.float)
a[:] = 0.1
print(a)
# [[0.1 0.1 0.1]
#  [0.1 0.1 0.1]]
