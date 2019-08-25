import numpy as np
from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
from scipy.sparse import csr_matrix

n = 100
c = n * 2
np.random.seed(1)
d = np.random.randint(0, n, c)
i = np.random.randint(0, n, c)
j = np.random.randint(0, n, c)

csr = csr_matrix((d, (i, j)), shape=(n, n))
a = csr.toarray()

print(a.shape)
# (100, 100)

print((a > 0).sum())
# 198

%%timeit
shortest_path(a)
# 2.3 ms ± 73.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
shortest_path(csr)
# 1.52 ms ± 21.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
shortest_path(a, method='D')
# 2.25 ms ± 65.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
shortest_path(csr, method='D')
# 1.51 ms ± 25.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dijkstra(a)
# 1.9 ms ± 52.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
dijkstra(csr)
# 1.4 ms ± 13.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
shortest_path(a, method='FW')
# 1.11 ms ± 33.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
shortest_path(csr, method='FW')
# 555 µs ± 71.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
floyd_warshall(a)
# 737 µs ± 13.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
floyd_warshall(csr)
# 433 µs ± 22.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dijkstra(a, indices=0)
# 590 µs ± 28.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
dijkstra(csr, indices=0)
# 111 µs ± 6.29 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

a_n = a.copy()
a_n[0, 1] = -10
csr_n = csr_matrix(a_n)

%%timeit
johnson(csr_n)
# 1.5 ms ± 17.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
bellman_ford(csr_n)
# 6.12 ms ± 141 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
floyd_warshall(csr_n)
# 402 µs ± 16.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
johnson(csr_n, indices=0)
# 201 µs ± 6.84 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
