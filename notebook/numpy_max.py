import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.max())
# 5

print(a.max(axis=0))
# [3 4 5]

print(a.max(axis=1))
# [2 5]
