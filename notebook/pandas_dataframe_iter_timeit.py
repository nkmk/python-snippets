import pandas as pd

df = pd.DataFrame(pd.np.arange(1000).reshape(100, 10))
print(df.shape)
# (100, 10)

print(df.head())
#     0   1   2   3   4   5   6   7   8   9
# 0   0   1   2   3   4   5   6   7   8   9
# 1  10  11  12  13  14  15  16  17  18  19
# 2  20  21  22  23  24  25  26  27  28  29
# 3  30  31  32  33  34  35  36  37  38  39
# 4  40  41  42  43  44  45  46  47  48  49

print(df.tail())
#       0    1    2    3    4    5    6    7    8    9
# 95  950  951  952  953  954  955  956  957  958  959
# 96  960  961  962  963  964  965  966  967  968  969
# 97  970  971  972  973  974  975  976  977  978  979
# 98  980  981  982  983  984  985  986  987  988  989
# 99  990  991  992  993  994  995  996  997  998  999

%%timeit
for i, row in df.iterrows():
    pass
# 4.53 ms ± 325 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
for t in df.itertuples():
    pass
# 981 µs ± 43.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
for t in df.itertuples(name=None):
    pass
# 718 µs ± 10.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
for i in df[0]:
    pass
# 15.6 µs ± 446 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
for i, j, k in zip(df[0], df[4], df[9]):
    pass
# 46.1 µs ± 588 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
for t in zip(df[0], df[1], df[2], df[3], df[4], df[5], df[6], df[7], df[8], df[9]):
    pass
# 147 µs ± 3.78 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
