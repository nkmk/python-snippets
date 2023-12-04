import pandas as pd

print(pd.__version__)
# 2.1.2

s = pd.Series([1, 10, 100])
print(s)
# 0      1
# 1     10
# 2    100
# dtype: int64

print(s.map(hex))
# 0     0x1
# 1     0xa
# 2    0x64
# dtype: object

def my_func(x):
    return x * 10

print(s.map(my_func))
# 0      10
# 1     100
# 2    1000
# dtype: int64

print(s.map(lambda x: x * 10))
# 0      10
# 1     100
# 2    1000
# dtype: int64

print(s * 10)
# 0      10
# 1     100
# 2    1000
# dtype: int64

s_nan = pd.Series([1, float('nan'), 100])
print(s_nan)
# 0      1.0
# 1      NaN
# 2    100.0
# dtype: float64

# print(s_nan.map(lambda x: hex(int(x))))
# ValueError: cannot convert float NaN to integer

print(s_nan.map(lambda x: hex(int(x)), na_action='ignore'))
# 0     0x1
# 1     NaN
# 2    0x64
# dtype: object

s = pd.Series(['11', 'AA', 'FF'])
print(s)
# 0    11
# 1    AA
# 2    FF
# dtype: object

# print(s.map(int, base=16))
# TypeError: Series.map() got an unexpected keyword argument 'base'

print(s.map(lambda x: int(x, 16)))
# 0     17
# 1    170
# 2    255
# dtype: int64

print(s.apply(int, base=16))
# 0     17
# 1    170
# 2    255
# dtype: int64

print(s.apply(int, args=(16,)))
# 0     17
# 1    170
# 2    255
# dtype: int64
