import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

a_slice = a[:, :2]
print(a_slice)
# [[0 1]
#  [3 4]]

print(np.shares_memory(a, a_slice))
# True

a_slice[0, 0] = 100
print(a_slice)
# [[100   1]
#  [  3   4]]

print(a)
# [[100   1   2]
#  [  3   4   5]]

a[0, 0] = 0
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a_slice)
# [[0 1]
#  [3 4]]

a_boolean_index = a[:, [True, False, True]]
print(a_boolean_index)
# [[0 2]
#  [3 5]]

print(np.shares_memory(a, a_boolean_index))
# False

a_boolean_index[0, 0] = 100
print(a_boolean_index)
# [[100   2]
#  [  3   5]]

print(a)
# [[0 1 2]
#  [3 4 5]]

a_slice_copy = a[:, :2].copy()
print(a_slice_copy)
# [[0 1]
#  [3 4]]

print(np.shares_memory(a, a_slice_copy))
# False

a_slice_copy[0, 0] = 100
print(a_slice_copy)
# [[100   1]
#  [  3   4]]

print(a)
# [[0 1 2]
#  [3 4 5]]

a_boolean_index_view = a[:, [True, False, True]].view()
print(a_boolean_index_view)
# [[0 2]
#  [3 5]]

print(np.shares_memory(a, a_boolean_index_view))
# False

a_boolean_index_view[0, 0] = 100
print(a_boolean_index_view)
# [[100   2]
#  [  3   5]]

print(a)
# [[0 1 2]
#  [3 4 5]]

a_fancy_index_slice = a[:, [0, 2]]
print(a_fancy_index_slice)
# [[0 2]
#  [3 5]]

print(np.shares_memory(a, a_fancy_index_slice))
# False

a_scalar_slice = a[1, :2]
print(a_scalar_slice)
# [3 4]

print(np.shares_memory(a, a_scalar_slice))
# True
