import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

n = 1000

np.random.seed(0)
d = np.ones(n, dtype=int)
i = np.random.randint(0, n, n)
j = np.random.randint(0, n, n)

print(d[:10])
print(i[:10])
print(j[:10])
# [1 1 1 1 1 1 1 1 1 1]
# [684 559 629 192 835 763 707 359   9 723]
# [ 20 683 630 128 484 365 105 706 225 652]

%%timeit
csr = csr_matrix((d, (i, j)), (n, n))
# 261 µs ± 8.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
csc = csc_matrix((d, (i, j)), (n, n))
# 256 µs ± 4.81 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
coo = coo_matrix((d, (i, j)), (n, n))
# 51.7 µs ± 1.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csr = coo_matrix((d, (i, j)), (n, n)).tocsr()
# 182 µs ± 1.98 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csc = coo_matrix((d, (i, j)), (n, n)).tocsc()
# 182 µs ± 1.29 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
lil = lil_matrix((n, n))
for d_, i_, j_ in zip(d, i, j):
    lil[i_, j_] = d_
# 4.87 ms ± 53.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
lil = lil_matrix((n, n))
# 409 µs ± 58.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
for d_, i_, j_ in zip(d, i, j):
    pass
# 314 µs ± 10.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

dij = list(zip(d, i, j))
print(dij[:5])
# [(1, 684, 20), (1, 559, 683), (1, 629, 630), (1, 192, 128), (1, 835, 484)]

%%timeit
lil = lil_matrix((n, n))
for d, i, j in dij:
    lil[i, j] = d
# 4.78 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
d_, i_, j_ = zip(*dij)
coo = coo_matrix((d_, (i_, j_)), (n, n))
# 522 µs ± 26.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dij_ = []
for t in dij:
    dij_.append(t)
d_, i_, j_ = zip(*dij_)
coo = coo_matrix((d_, (i_, j_)), (n, n))
# 548 µs ± 6.26 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
d_ = []
i_ = []
j_ = []
for d, i, j in dij:
    d_.append(d)
    i_.append(i)
    j_.append(j)
coo = coo_matrix((d_, (i_, j_)), (n, n))
# 636 µs ± 6.56 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

a = coo_matrix((d, (i, j)), (n, n)).toarray()
print(a.shape)
# (1000, 1000)

%%timeit
csr = csr_matrix(a)
# 6.11 ms ± 351 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csc = csc_matrix(a)
# 6.16 ms ± 239 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
coo = coo_matrix(a)
# 6.02 ms ± 433 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
lil = lil_matrix(a)
# 7.98 ms ± 200 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
lil = coo_matrix(a).tolil()
# 7.96 ms ± 478 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
