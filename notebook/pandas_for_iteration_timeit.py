import pandas as pd
import numpy as np

print(pd.__version__)
# 2.1.4

print(np.__version__)
# 1.26.2

df = pd.DataFrame(np.arange(1000).reshape(100, 10))
print(df.shape)
# (100, 10)

print(df.head(3))
#     0   1   2   3   4   5   6   7   8   9
# 0   0   1   2   3   4   5   6   7   8   9
# 1  10  11  12  13  14  15  16  17  18  19
# 2  20  21  22  23  24  25  26  27  28  29

print(df.tail(3))
#       0    1    2    3    4    5    6    7    8    9
# 97  970  971  972  973  974  975  976  977  978  979
# 98  980  981  982  983  984  985  986  987  988  989
# 99  990  991  992  993  994  995  996  997  998  999

%%timeit
for i, row in df.iterrows():
    pass
# 735 µs ± 20.5 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
for t in df.itertuples():
    pass
# 202 µs ± 1.74 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%%timeit
for t in df.itertuples(name=None):
    pass
# 148 µs ± 780 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%%timeit
for i in df[0]:
    pass
# 4.27 µs ± 30.3 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
for i, j, k in zip(df[0], df[4], df[9]):
    pass
# 13.5 µs ± 53.4 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
for t in zip(df[0], df[1], df[2], df[3], df[4], df[5], df[6], df[7], df[8], df[9]):
    pass
# 41.3 µs ± 281 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
