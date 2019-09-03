n_small = 10
n_large = 10000

l_small = list(range(n_small))
l_large = list(range(n_large))

%%timeit
-1 in l_small
# 178 ns ± 4.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
-1 in l_large
# 128 µs ± 11.5 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
0 in l_large
# 33.4 ns ± 0.397 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
5000 in l_large
# 66.1 µs ± 4.38 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
9999 in l_large
# 127 µs ± 2.17 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

s_small = set(l_small)
s_large = set(l_large)

%%timeit
-1 in s_small
# 40.4 ns ± 0.572 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
-1 in s_large
# 39.4 ns ± 1.1 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
0 in s_large
# 39.7 ns ± 1.27 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
5000 in s_large
# 53.1 ns ± 0.974 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
9999 in s_large
# 52.4 ns ± 0.403 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%%timeit
for i in range(n_large):
    i in l_large
# 643 ms ± 29.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
s_large_ = set(l_large)
for i in range(n_large):
    i in s_large_
# 746 µs ± 6.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

d = dict(zip(l_large, l_large))
print(len(d))
# 10000

print(d[0])
# 0

print(d[9999])
# 9999

%%timeit
for i in range(n_large):
    i in d
# 756 µs ± 24.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

dv = d.values()

%%timeit
for i in range(n_large):
    i in dv
# 990 ms ± 28.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

di = d.items()

%%timeit
for i in range(n_large):
    (i, i) in di
# 1.18 ms ± 26.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
