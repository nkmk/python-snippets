import numpy as np
import pandas as pd

print(np.__version__)
# 1.26.1

print(pd.__version__)
# 2.1.2

s = pd.Series([-0.5, -0.25, 0.25, 0.5])
print(s)
# 0   -0.50
# 1   -0.25
# 2    0.25
# 3    0.50
# dtype: float64

print(np.floor(s))
# 0   -1.0
# 1   -1.0
# 2    0.0
# 3    0.0
# dtype: float64

print(np.trunc(s))
# 0   -0.0
# 1   -0.0
# 2    0.0
# 3    0.0
# dtype: float64

print(np.ceil(s))
# 0   -0.0
# 1   -0.0
# 2    1.0
# 3    1.0
# dtype: float64

def my_round(x, decimals=0):
    return np.floor(x * 10**decimals + 0.5) / 10**decimals

s = pd.Series([0.5, 1.5, 2.5, 3.5, 4.5])
print(s)
# 0    0.5
# 1    1.5
# 2    2.5
# 3    3.5
# 4    4.5
# dtype: float64

print(my_round(s))
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# dtype: float64

print(my_round(s * 10, -1))
# 0    10.0
# 1    20.0
# 2    30.0
# 3    40.0
# 4    50.0
# dtype: float64

df = pd.DataFrame({'f': [123.456, 987.654], 'i': [123, 987], 's': ['abc', 'xyz']})
print(df)
#          f    i    s
# 0  123.456  123  abc
# 1  987.654  987  xyz

# print(np.floor(df))
# TypeError: must be real number, not str

print(np.floor(df.select_dtypes('number')))
#        f      i
# 0  123.0  123.0
# 1  987.0  987.0

df['f_floor'] = np.floor(df['f'])
print(df)
#          f    i    s  f_floor
# 0  123.456  123  abc    123.0
# 1  987.654  987  xyz    987.0
