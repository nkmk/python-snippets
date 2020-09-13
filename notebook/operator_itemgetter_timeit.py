import operator

l = [{'k1': i} for i in range(10000)]

print(len(l))
# 10000

print(l[:5])
# [{'k1': 0}, {'k1': 1}, {'k1': 2}, {'k1': 3}, {'k1': 4}]

print(l[-5:])
# [{'k1': 9995}, {'k1': 9996}, {'k1': 9997}, {'k1': 9998}, {'k1': 9999}]

%%timeit
sorted(l, key=lambda x: x['k1'])
# 1.09 ms ± 35 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
sorted(l, key=operator.itemgetter('k1'))
# 716 µs ± 28.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
sorted(l, key=lambda x: x['k1'], reverse=True)
# 1.11 ms ± 41.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
sorted(l, key=operator.itemgetter('k1'), reverse=True)
# 768 µs ± 58.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
max(l, key=lambda x: x['k1'])
# 1.33 ms ± 130 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
max(l, key=operator.itemgetter('k1'))
# 813 µs ± 54.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
min(l, key=lambda x: x['k1'])
# 1.27 ms ± 69.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
min(l, key=operator.itemgetter('k1'))
# 824 µs ± 83.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
