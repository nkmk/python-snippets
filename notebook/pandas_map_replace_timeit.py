import pandas as pd

print(pd.__version__)
# 2.1.2

s = pd.Series(range(100))

d_100 = {i: i * 10 for i in range(100)}

%%timeit
s.map(d_100)
# 70.7 µs ± 2.08 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%%timeit
s.replace(d_100)
# 1.31 ms ± 26.7 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

d_50 = {i: i * 10 for i in range(50)}

%%timeit
s.map(d_50).fillna(s)
# 108 µs ± 3.1 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%%timeit
s.replace(d_50)
# 653 µs ± 3.73 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

d_5 = {i: i * 10 for i in range(5)}

%%timeit
s.map(d_5).fillna(s)
# 104 µs ± 3.85 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%%timeit
s.replace(d_5)
# 78.5 µs ± 860 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
