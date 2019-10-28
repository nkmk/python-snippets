import numpy as np

a_inf = np.array([-np.inf, 0, np.inf])
print(a_inf)
# [-inf   0.  inf]

print(np.isinf(a_inf))
# [ True False  True]

print(a_inf == np.inf)
# [False False  True]

print(a_inf == -np.inf)
# [ True False False]
