from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, dok_matrix, eye

n = 1000

csr = eye(n, format='csr')
csc = eye(n, format='csc')
lil = eye(n, format='lil')
dok = eye(n, format='dok')

%%timeit
csr.getrow(0)
# 48.3 µs ± 2.71 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc.getrow(0)
# 139 µs ± 11.6 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil.getrow(0)
# 18.1 µs ± 522 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok.getrow(0)
# 700 µs ± 60.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr[0]
# 78.3 µs ± 5.64 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[0]
# 74.5 µs ± 715 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[0]
# 43.9 µs ± 4.06 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[0]
# 462 µs ± 16.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr.getcol(0)
# 67.5 µs ± 7.8 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc.getcol(0)
# 49.4 µs ± 2.21 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil.getcol(0)
# 955 µs ± 15.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dok.getcol(0)
# 12.3 ms ± 154 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr[:, 0]
# 86.7 µs ± 7.77 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:, 0]
# 77 µs ± 6.75 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:, 0]
# 442 µs ± 31.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dok[:, 0]
# 929 µs ± 36.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr[0, 0]
# 31.8 µs ± 454 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[0, 0]
# 104 µs ± 5.93 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[0, 0]
# 3.37 µs ± 123 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
dok[0, 0]
# 18.1 µs ± 134 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
csr[:10]
# 71.4 µs ± 929 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:10]
# 184 µs ± 8.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:10]
# 47.2 µs ± 1.57 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[:10]
# 632 µs ± 7.13 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr[:, :10]
# 77.5 µs ± 1.32 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:, :10]
# 74.9 µs ± 5.32 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:, :10]
# 420 µs ± 14.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dok[:, :10]
# 905 µs ± 6.62 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csr[:10, :10]
# 73.9 µs ± 1.63 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc[:10, :10]
# 178 µs ± 1.79 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil[:10, :10]
# 47.5 µs ± 925 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
dok[:10, :10]
# 210 µs ± 6.29 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
