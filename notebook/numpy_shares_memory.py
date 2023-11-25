import numpy as np

print(np.__version__)
# 1.26.1

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

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

a_0 = a[::2]
print(a_0)
# [0 2 4 6 8]

a_1 = a[1::2]
print(a_1)
# [1 3 5 7 9]

print(np.shares_memory(a_0, a_1))
# False

print(np.may_share_memory(a_0, a_1))
# True

a_2 = a[:5]
print(a_2)
# [0 1 2 3 4]

a_3 = a[5:]
print(a_3)
# [5 6 7 8 9]

print(np.shares_memory(a_2, a_3))
# False

print(np.may_share_memory(a_2, a_3))
# False

%%timeit
np.shares_memory(a_0, a_1)
# 200 ns ± 1.1 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

%%timeit
np.may_share_memory(a_0, a_1)
# 123 ns ± 0.284 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
