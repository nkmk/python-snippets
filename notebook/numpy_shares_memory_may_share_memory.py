import numpy as np

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
# 839 ns ± 53.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
np.may_share_memory(a_0, a_1)
# 275 ns ± 5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
