import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

%%timeit
a.ravel()
# 242 ns ± 2.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
a.flatten()
# 725 ns ± 45.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
a.reshape(-1)
# 851 ns ± 13.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

a_large = np.arange(1000000).reshape(100, 100, 100)

%%timeit
a_large.ravel()
# 242 ns ± 3.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
a_large.flatten()
# 2.03 ms ± 8.63 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
a_large.reshape(-1)
# 899 ns ± 52 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
