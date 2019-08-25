from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix

l = [[0, 8, 0, 3],
     [0, 0, 2, 5],
     [0, 0, 0, 6],
     [0, 0, 0, 0]]

%%timeit
minimum_spanning_tree(l)
# 378 µs ± 9.78 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
minimum_spanning_tree(l, True)
# 383 µs ± 16.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

csr = csr_matrix(l)

%%timeit
minimum_spanning_tree(csr)
# 158 µs ± 5.95 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
minimum_spanning_tree(csr, True)
# 108 µs ± 2.19 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

coo = coo_matrix(l)

%%timeit
minimum_spanning_tree(coo)
# 185 µs ± 11.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
minimum_spanning_tree(coo, True)
# 184 µs ± 9.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
minimum_spanning_tree(csr_matrix(l))
# 364 µs ± 4.11 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
minimum_spanning_tree(csr_matrix(l), True)
# 319 µs ± 11.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

mst = minimum_spanning_tree(csr, True)

print(csr)
#   (0, 3)	8
#   (1, 2)	3
#   (1, 3)	2
#   (1, 3)	5
#   (2, 3)	6

print(mst)
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0
