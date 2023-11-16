import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

%%timeit
a.ravel()
# 43.6 ns ± 0.298 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
a.flatten()
# 249 ns ± 0.971 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

%%timeit
a.reshape(-1)
# 80.2 ns ± 0.145 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

a_large = np.arange(1000000).reshape(100, 100, 100)

%%timeit
a_large.ravel()
# 43.6 ns ± 0.118 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
a_large.flatten()
# 423 µs ± 25.9 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
a_large.reshape(-1)
# 80 ns ± 0.0587 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
