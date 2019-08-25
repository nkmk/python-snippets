import numpy as np
from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
from scipy.sparse import csr_matrix

n = 100
c = n * 50
np.random.seed(1)
d = np.random.randint(0, n, c)
i = np.random.randint(0, n, c)
j = np.random.randint(0, n, c)

csr = csr_matrix((d, (i, j)), shape=(n, n))
a = csr.toarray()

print(a.shape)
# (100, 100)

print((a > 0).sum())
# 3945

%%timeit
shortest_path(a)
# 2.59 ms ± 132 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
shortest_path(csr)
# 1.73 ms ± 18.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
shortest_path(a, method='FW')
# 2.57 ms ± 173 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
shortest_path(csr, method='FW')
# 1.73 ms ± 21.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
floyd_warshall(a)
# 1.92 ms ± 30.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
floyd_warshall(csr)
# 1.61 ms ± 17 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dijkstra(a, indices=0)
# 762 µs ± 29.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dijkstra(csr, indices=0)
# 164 µs ± 4.85 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

a_n = a.copy()
a_n[0, 1] = -10
csr_n = csr_matrix(a_n)

%%timeit
johnson(csr_n)
# 6.53 ms ± 72.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
bellman_ford(csr_n)
# 79.8 ms ± 354 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
floyd_warshall(csr_n)
# 1.57 ms ± 15.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
johnson(csr_n, indices=0)
# 952 µs ± 11.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
