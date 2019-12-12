import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(np.expand_dims(a, 0))
# [[[0 1 2]
#   [3 4 5]]]

print(np.expand_dims(a, 0).shape)
# (1, 2, 3)

print(np.expand_dims(a, 1).shape)
# (2, 1, 3)

print(np.expand_dims(a, 2).shape)
# (2, 3, 1)

print(np.expand_dims(a, -1).shape)
# (2, 3, 1)

print(np.expand_dims(a, -2).shape)
# (2, 1, 3)

print(np.expand_dims(a, -3).shape)
# (1, 2, 3)

print(np.expand_dims(a, 3).shape)
# (2, 3, 1)
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: Both axis > a.ndim and axis < -a.ndim - 1 are deprecated and will raise an AxisError in the future.
#   """Entry point for launching an IPython kernel.

print(np.expand_dims(a, -4).shape)
# (2, 1, 3)
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: Both axis > a.ndim and axis < -a.ndim - 1 are deprecated and will raise an AxisError in the future.
#   """Entry point for launching an IPython kernel.

# print(np.expand_dims(a, (0, 1)).shape)
# TypeError: '>' not supported between instances of 'tuple' and 'int'

a_expand_dims = np.expand_dims(a, 0)

print(np.shares_memory(a, a_expand_dims))
# True
