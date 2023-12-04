import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.2

print(np.__version__)
# 1.26.1

df = pd.DataFrame(np.arange(-5000, 5000).reshape(100, 100))

print(df.shape)
# (100, 100)

%%timeit
df.map(abs)
# 2.07 ms ± 16.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
df.abs()
# 5.06 µs ± 55 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
np.abs(df)
# 7.81 µs ± 120 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
df.apply(sum)
# 932 µs ± 95.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
df.apply(sum, raw=True)
# 427 µs ± 4.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
df.sum()
# 35 µs ± 140 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%%timeit
np.sum(df, axis=0)
# 37.3 µs ± 66.9 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
