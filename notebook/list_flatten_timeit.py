import itertools

l_2d_5 = [[0, 1, 2]] * 5
print(l_2d_5)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

%%timeit
list(itertools.chain.from_iterable(l_2d_5))
# 711 ns ± 21.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
sum(l_2d_5, [])
# 448 ns ± 10.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

l_2d_100 = [[0, 1, 2]] * 100

%%timeit
list(itertools.chain.from_iterable(l_2d_100))
# 7.27 µs ± 390 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
sum(l_2d_100, [])
# 41 µs ± 1.34 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

l_2d_10000 = [[0, 1, 2]] * 10000

%%timeit
list(itertools.chain.from_iterable(l_2d_10000))
# 513 µs ± 15.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
sum(l_2d_10000, [])
# 418 ms ± 22.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
