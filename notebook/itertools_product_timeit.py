import itertools

A = range(1000)

%%timeit
for x in itertools.product(A, A):
    pass
# 30.8 ms ± 910 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for a1, a2 in itertools.product(A, A):
    pass
# 22.8 ms ± 293 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for a1 in A:
    for a2 in A:
        pass
# 22.6 ms ± 345 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for x in ((a1, a2) for a1 in A for a2 in A):
    pass
# 82.2 ms ± 467 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for a1, a2 in ((a1, a2) for a1 in A for a2 in A):
    pass
# 91.4 ms ± 276 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
v = 0
for a1, a2 in itertools.product(A, A):
    v += a1 * a2
# 98.8 ms ± 579 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
v = 0
for a1 in A:
    for a2 in A:
        v += a1 * a2
# 95.7 ms ± 4.05 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
v = sum(a1 * a2 for a1, a2 in itertools.product(A, A))
# 94 ms ± 2.36 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
v = sum(a1 * a2 for a1 in A for a2 in A)
# 92.7 ms ± 4.83 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

B = range(100)

%%timeit
for x in itertools.product(B, B, B):
    pass
# 31.6 ms ± 725 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for b1, b2, b3 in itertools.product(B, B, B):
    pass
# 26.2 ms ± 490 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for b1 in B:
    for b2 in B:
        for b3 in B:
            pass
# 12.9 ms ± 176 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
for x in ((b1, b2, b3) for b1 in B for b2 in B for b3 in B):
    pass
# 80.9 ms ± 1.27 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for b1, b2, b3 in ((b1, b2, b3) for b1 in B for b2 in B for b3 in B):
    pass
# 93.8 ms ± 3.22 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
