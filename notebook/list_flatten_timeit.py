import itertools

l_2d_5 = [[0, 1, 2] for i in range(5)]
print(l_2d_5)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

%%timeit
list(itertools.chain.from_iterable(l_2d_5))
# 537 ns ± 4.59 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
sum(l_2d_5, [])
# 319 ns ± 1.85 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
[x for row in l_2d_5 for x in row]
# 764 ns ± 32.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

l_2d_100 = [[0, 1, 2] for i in range(100)]

%%timeit
list(itertools.chain.from_iterable(l_2d_100))
# 6.94 µs ± 139 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
sum(l_2d_100, [])
# 35.5 µs ± 1.2 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
[x for row in l_2d_100 for x in row]
# 13.5 µs ± 959 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

l_2d_10000 = [[0, 1, 2] for i in range(10000)]

%%timeit
list(itertools.chain.from_iterable(l_2d_10000))
# 552 µs ± 79.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
sum(l_2d_10000, [])
# 343 ms ± 2.19 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
[x for row in l_2d_10000 for x in row]
# 1.11 ms ± 110 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
