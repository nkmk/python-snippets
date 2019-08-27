l = list(range(100000))
print(l[:5])
# [0, 1, 2, 3, 4]

print(l[-5:])
# [99995, 99996, 99997, 99998, 99999]

print(len(l))
# 100000

%%timeit
all([i < 0 for i in l])
# 4.15 ms ± 117 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
all(i < 0 for i in l)
# 469 ns ± 6.12 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
all([i >= 0 for i in l])
# 4.5 ms ± 57.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
all(i >= 0 for i in l)
# 5.49 ms ± 255 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
all(i < 50000 for i in l)
# 2.73 ms ± 37.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
any([i >= 0 for i in l])
# 4.2 ms ± 183 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
any(i >= 0 for i in l)
# 468 ns ± 4.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit
any([i < 0 for i in l])
# 4.56 ms ± 180 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
any(i < 0 for i in l)
# 5.33 ms ± 45.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
any(i > 50000 for i in l)
# 2.78 ms ± 120 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
