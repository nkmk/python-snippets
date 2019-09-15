import numpy as np

a = np.arange(6)
print(a)
# [0 1 2 3 4 5]

a_reshape = a.reshape(2, 3)
print(a_reshape)
# [[0 1 2]
#  [3 4 5]]

print(np.shares_memory(a, a_reshape))
# True

a_slice = a[2:5]
print(a_slice)
# [2 3 4]

print(np.shares_memory(a_reshape, a_slice))
# True

a_reshape_copy = a.reshape(2, 3).copy()
print(a_reshape_copy)
# [[0 1 2]
#  [3 4 5]]

print(np.shares_memory(a, a_reshape_copy))
# False
