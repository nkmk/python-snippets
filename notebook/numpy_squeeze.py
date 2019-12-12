import numpy as np

a = np.arange(6).reshape(1, 2, 1, 3, 1)
print(a)
# [[[[[0]
#     [1]
#     [2]]]
# 
# 
#   [[[3]
#     [4]
#     [5]]]]]

print(a.shape)
# (1, 2, 1, 3, 1)

a_s = np.squeeze(a)
print(a_s)
# [[0 1 2]
#  [3 4 5]]

print(a_s.shape)
# (2, 3)

print(np.shares_memory(a, a_s))
# True

a_s_copy = np.squeeze(a).copy()

print(np.shares_memory(a, a_s_copy))
# False

print(np.squeeze(a, 0))
# [[[[0]
#    [1]
#    [2]]]
# 
# 
#  [[[3]
#    [4]
#    [5]]]]

print(np.squeeze(a, 0).shape)
# (2, 1, 3, 1)

# print(np.squeeze(a, 1))
# ValueError: cannot select an axis to squeeze out which has size not equal to one

# print(np.squeeze(a, 5))
# AxisError: axis 5 is out of bounds for array of dimension 5

print(np.squeeze(a, -1))
# [[[[0 1 2]]
# 
#   [[3 4 5]]]]

print(np.squeeze(a, -1).shape)
# (1, 2, 1, 3)

print(np.squeeze(a, -3))
# [[[[0]
#    [1]
#    [2]]
# 
#   [[3]
#    [4]
#    [5]]]]

print(np.squeeze(a, -3).shape)
# (1, 2, 3, 1)

print(np.squeeze(a, (0, -1)))
# [[[0 1 2]]
# 
#  [[3 4 5]]]

print(np.squeeze(a, (0, -1)).shape)
# (2, 1, 3)

# print(np.squeeze(a, (0, 1)))
# ValueError: cannot select an axis to squeeze out which has size not equal to one

print(a.squeeze())
# [[0 1 2]
#  [3 4 5]]

print(a.squeeze().shape)
# (2, 3)

print(a.squeeze((0, -1)))
# [[[0 1 2]]
# 
#  [[3 4 5]]]

print(a.squeeze((0, -1)).shape)
# (2, 1, 3)

a_s = a.squeeze()
print(a_s)
# [[0 1 2]
#  [3 4 5]]

print(np.shares_memory(a, a_s))
# True

print(a)
# [[[[[0]
#     [1]
#     [2]]]
# 
# 
#   [[[3]
#     [4]
#     [5]]]]]
