import collections

l_100 = list(range(100))

%%timeit
collections.Counter(l_100)
# 7.36 µs ± 205 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

l_10000 = list(range(10000))

%%timeit
collections.Counter(l_10000)
# 435 µs ± 22.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

l_10000_2 = list(range(100)) * 100
print(len(l_10000_2))
# 10000

%%timeit
collections.Counter(l_10000_2)
# 366 µs ± 3.86 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
