import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, dok_matrix

n = 1000

np.random.seed(0)
d = np.random.randint(1, n, n*10)
i = np.random.randint(0, n, n*10)
j = np.random.randint(0, n, n*10)

csr = csr_matrix((d, (i, j)), (n, n))
csc = csr.tocsc()
lil = csr.tolil()
dok = csr.todok()

%%timeit
csr.getrow(0)
# 54.4 µs ± 3.65 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc.getrow(0)
# 184 µs ± 14.7 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil.getrow(0)
# 18.8 µs ± 672 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok.getrow(0)
# 2.18 ms ± 85.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr[0]
# 75.3 µs ± 3.24 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[0]
# 112 µs ± 5.41 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[0]
# 41.8 µs ± 3.52 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[0]
# 312 µs ± 4.88 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr.getcol(0)
# 83.2 µs ± 6.69 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc.getcol(0)
# 57.2 µs ± 1.66 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil.getcol(0)
# 2.77 ms ± 172 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
dok.getcol(0)
# 2.53 ms ± 340 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr[:, 0]
# 115 µs ± 2.47 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:, 0]
# 84.1 µs ± 5.81 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:, 0]
# 465 µs ± 12.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dok[:, 0]
# 636 µs ± 34 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr[0, 0]
# 22.8 µs ± 1.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[0, 0]
# 24.5 µs ± 1.68 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[0, 0]
# 3.64 µs ± 57.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
dok[0, 0]
# 12.3 µs ± 568 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
csr[:10]
# 75.2 µs ± 2.23 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:10]
# 118 µs ± 6.03 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:10]
# 54.3 µs ± 5.2 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[:10]
# 5.05 ms ± 440 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr[:, :10]
# 117 µs ± 15 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:, :10]
# 91.4 µs ± 10.3 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:, :10]
# 481 µs ± 37.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dok[:, :10]
# 9.12 ms ± 257 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr[:10, :10]
# 80.4 µs ± 5.21 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:10, :10]
# 75.5 µs ± 2.46 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:10, :10]
# 47.6 µs ± 2.13 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[:10, :10]
# 70.5 µs ± 4.92 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
