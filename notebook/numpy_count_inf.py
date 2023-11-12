import numpy as np

print(np.__version__)
# 1.26.1

a_inf = np.array([-np.inf, 0, np.inf])
print(a_inf)
# [-inf   0.  inf]

print(np.isinf(a_inf))
# [ True False  True]

print(np.isposinf(a_inf))
# [False False  True]

print(np.isneginf(a_inf))
# [ True False False]

print(a_inf == np.inf)
# [False False  True]

print(a_inf == -np.inf)
# [ True False False]

print(np.count_nonzero(np.isinf(a_inf)))
# 2

print(np.count_nonzero(np.isposinf(a_inf)))
# 1

print(np.count_nonzero(np.isneginf(a_inf)))
# 1
