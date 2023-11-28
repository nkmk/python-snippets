import pandas as pd

print(pd.__version__)
# 2.1.2

s_f = pd.Series([123.456, 987.654])
print(s_f)
# 0    123.456
# 1    987.654
# dtype: float64

print(s_f.round())
# 0    123.0
# 1    988.0
# dtype: float64

print(s_f.round().astype(int))
# 0    123
# 1    988
# dtype: int64

print(s_f.round(2))
# 0    123.46
# 1    987.65
# dtype: float64

print(s_f.round(-2))
# 0     100.0
# 1    1000.0
# dtype: float64

s_i = pd.Series([123, 987])
print(s_i)
# 0    123
# 1    987
# dtype: int64

print(s_i.round())
# 0    123
# 1    987
# dtype: int64

print(s_i.round(2))
# 0    123
# 1    987
# dtype: int64

print(s_i.round(-2))
# 0     100
# 1    1000
# dtype: int64

s_i_round = s_i.round(-2)
print(s_i_round)
# 0     100
# 1    1000
# dtype: int64

print(s_i)
# 0    123
# 1    987
# dtype: int64

df = pd.DataFrame({'f': [123.456, 987.654], 'i': [123, 987], 's': ['abc', 'xyz']})
print(df)
#          f    i    s
# 0  123.456  123  abc
# 1  987.654  987  xyz

print(df.dtypes)
# f    float64
# i      int64
# s     object
# dtype: object

print(df.round())
#        f    i    s
# 0  123.0  123  abc
# 1  988.0  987  xyz

print(df.round(2))
#         f    i    s
# 0  123.46  123  abc
# 1  987.65  987  xyz

print(df.round(-2))
#         f     i    s
# 0   100.0   100  abc
# 1  1000.0  1000  xyz

print(df.round({'f': 2, 'i': -1, 's': 2}))
#         f    i    s
# 0  123.46  120  abc
# 1  987.65  990  xyz

print(df.round({'i': -2}))
#          f     i    s
# 0  123.456   100  abc
# 1  987.654  1000  xyz

s = pd.Series([0.5, 1.5, 2.5, 3.5, 4.5])
print(s)
# 0    0.5
# 1    1.5
# 2    2.5
# 3    3.5
# 4    4.5
# dtype: float64

print(s.round())
# 0    0.0
# 1    2.0
# 2    2.0
# 3    4.0
# 4    4.0
# dtype: float64

s = pd.Series([2.49, 2.5, 2.51])
print(s)
# 0    2.49
# 1    2.50
# 2    2.51
# dtype: float64

print(s.round())
# 0    2.0
# 1    2.0
# 2    3.0
# dtype: float64

s = pd.Series([249, 250, 251])
print(s)
# 0    249
# 1    250
# 2    251
# dtype: int64

print(s.round(-2))
# 0    200
# 1    200
# 2    300
# dtype: int64
