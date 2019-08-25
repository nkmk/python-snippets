import numpy as np
from scipy.sparse import csr_matrix

a = np.eye(1000, dtype=np.int64)
print(type(a))
# <class 'numpy.ndarray'>

print(a[:10, :10])
# [[1 0 0 0 0 0 0 0 0 0]
#  [0 1 0 0 0 0 0 0 0 0]
#  [0 0 1 0 0 0 0 0 0 0]
#  [0 0 0 1 0 0 0 0 0 0]
#  [0 0 0 0 1 0 0 0 0 0]
#  [0 0 0 0 0 1 0 0 0 0]
#  [0 0 0 0 0 0 1 0 0 0]
#  [0 0 0 0 0 0 0 1 0 0]
#  [0 0 0 0 0 0 0 0 1 0]
#  [0 0 0 0 0 0 0 0 0 1]]

print(a.shape)
# (1000, 1000)

csr = csr_matrix(a)
print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

def get_size_of_csr(csr):
    return csr.data.nbytes + csr.indices.nbytes + csr.indptr.nbytes

print(a.nbytes)
# 8000000

print(get_size_of_csr(csr))
# 16004

%%timeit
a @ a
# 2.19 s ± 90.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
csr * csr
# 135 µs ± 5.34 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

a_dense = np.random.randint(1, 100, (1000, 1000))
csr_dense = csr_matrix(a_dense)

print(a_dense[:10, :10])
# [[98 46 10 41 53 34 82 91 77 82]
#  [30 21 18 89 30 20 60 88 54  5]
#  [44 91 92 34 21 75 55 21 60 44]
#  [90 30 57 52 14  5 64 62 41  7]
#  [59 37 79 21 37 77 45 74 43 61]
#  [10 73 92 98 39 72 72  4 82 81]
#  [26 48 64 93 81 78  3  6 52 52]
#  [28 85 42 19 51 61 23 81 89 79]
#  [32 78 24 84 28 67 80 38 85 64]
#  [98 11 48 85 17  5 87 30 90 22]]

print(a_dense.dtype)
# int64

print(a_dense.shape)
# (1000, 1000)

print(a_dense.nbytes)
# 8000000

print(get_size_of_csr(csr_dense))
# 12004004

%%timeit
a_dense @ a_dense
# 2.19 s ± 244 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
csr_dense * csr_dense
# 1.91 s ± 123 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

a_10_10 = np.eye(10, dtype=np.int64)
csr_10_10 = csr_matrix(a_10_10)

print(a_10_10.nbytes)
# 800

print(get_size_of_csr(csr_10_10))
# 164

%%timeit
a_10_10 @ a_10_10
# 2.23 µs ± 421 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
csr_10_10 * csr_10_10
# 112 µs ± 455 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

a_100_100 = np.eye(100, dtype=np.int64)
csr_100_100 = csr_matrix(a_100_100)

print(a_100_100.nbytes)
# 80000

print(get_size_of_csr(csr_100_100))
# 1604

%%timeit
a_100_100 @ a_100_100
# 49.3 µs ± 4.32 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
csr_100_100 * csr_100_100
# 115 µs ± 790 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

a_200_200 = np.eye(200, dtype=np.int64)
csr_200_200 = csr_matrix(a_200_200)

print(a_200_200.nbytes)
# 320000

print(get_size_of_csr(csr_200_200))
# 3204

%%timeit
a_200_200 @ a_200_200
# 6.08 ms ± 126 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
csr_200_200 * csr_200_200
# 132 µs ± 14.9 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
