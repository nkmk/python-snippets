l = list(range(100000))
print(l[:5])
# [0, 1, 2, 3, 4]

print(l[-5:])
# [99995, 99996, 99997, 99998, 99999]

print(len(l))
# 100000

%%timeit
all([i < 0 for i in l])
# 963 μs ± 22.8 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
all(i < 0 for i in l)
# 132 ns ± 4.21 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
all([i >= 0 for i in l])
# 1.11 ms ± 18.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
all(i >= 0 for i in l)
# 1.75 ms ± 2.53 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
all(i < 50000 for i in l)
# 882 μs ± 2.92 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
any([i >= 0 for i in l])
# 902 μs ± 5.31 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
any(i >= 0 for i in l)
# 123 ns ± 0.0354 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
any([i < 0 for i in l])
# 1.1 ms ± 2.88 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
any(i < 0 for i in l)
# 1.75 ms ± 6.04 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
any(i > 50000 for i in l)
# 897 μs ± 6.9 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
