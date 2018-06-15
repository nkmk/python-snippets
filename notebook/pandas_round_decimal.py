import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import platform

print(platform.python_version())
print(pd.__version__)
print(np.__version__)
# 3.6.5
# 0.23.0
# 1.14.3

s_f = pd.Series([123.456, 654.123])

print(s_f)
# 0    123.456
# 1    654.123
# dtype: float64

print(s_f.round())
# 0    123.0
# 1    654.0
# dtype: float64

print(s_f.round().astype(int))
# 0    123
# 1    654
# dtype: int64

print(s_f.round(2))
# 0    123.46
# 1    654.12
# dtype: float64

print(s_f.round(-2))
# 0    100.0
# 1    700.0
# dtype: float64

s_i = pd.Series([123, 654])

print(s_i)
# 0    123
# 1    654
# dtype: int64

print(s_i.round())
# 0    123
# 1    654
# dtype: int64

print(s_i.round(2))
# 0    123
# 1    654
# dtype: int64

print(s_i.round(-2))
# 0    100
# 1    700
# dtype: int64

s_i_round = s_i.round(-2)

print(s_i_round)
# 0    100
# 1    700
# dtype: int64

print(s_i)
# 0    123
# 1    654
# dtype: int64

df = pd.DataFrame({'f': [123.456, 654.321], 'i': [123, 654], 's': ['abc', 'xyz']})

print(df)
#          f    i    s
# 0  123.456  123  abc
# 1  654.321  654  xyz

print(df.dtypes)
# f    float64
# i      int64
# s     object
# dtype: object

print(df.round())
#        f    i    s
# 0  123.0  123  abc
# 1  654.0  654  xyz

print(df.round(2))
#         f    i    s
# 0  123.46  123  abc
# 1  654.32  654  xyz

print(df.round(-2))
#        f    i    s
# 0  100.0  100  abc
# 1  700.0  700  xyz

print(df.round({'f': 2, 'i': -1}))
#         f    i    s
# 0  123.46  120  abc
# 1  654.32  650  xyz

print(df.round({'i': -2}))
#          f    i    s
# 0  123.456  100  abc
# 1  654.321  700  xyz

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

s = pd.Series([5, 15, 25, 5.1, 15.1, 25.1])

print(s)
# 0     5.0
# 1    15.0
# 2    25.0
# 3     5.1
# 4    15.1
# 5    25.1
# dtype: float64

print(s.round(-1))
# 0     0.0
# 1    20.0
# 2    20.0
# 3    10.0
# 4    20.0
# 5    30.0
# dtype: float64

print('Python round')
print('0.005 => ', round(0.005, 2))
print('0.015 => ', round(0.015, 2))
print('0.025 => ', round(0.025, 2))
print('0.035 => ', round(0.035, 2))
print('0.045 => ', round(0.045, 2))
print('2.675 => ', round(2.675, 2))
# Python round
# 0.005 =>  0.01
# 0.015 =>  0.01
# 0.025 =>  0.03
# 0.035 =>  0.04
# 0.045 =>  0.04
# 2.675 =>  2.67

print('NumPy np.around (np.round)')
print('0.005 => ', np.around(0.005, 2))
print('0.015 => ', np.around(0.015, 2))
print('0.025 => ', np.around(0.025, 2))
print('0.035 => ', np.around(0.035, 2))
print('0.045 => ', np.around(0.045, 2))
print('2.675 => ', np.around(2.675, 2))
# NumPy np.around (np.round)
# 0.005 =>  0.0
# 0.015 =>  0.02
# 0.025 =>  0.02
# 0.035 =>  0.04
# 0.045 =>  0.04
# 2.675 =>  2.68

s = pd.Series([0.005, 0.015, 0.025, 0.035, 0.045, 2.675])

print(s)
# 0    0.005
# 1    0.015
# 2    0.025
# 3    0.035
# 4    0.045
# 5    2.675
# dtype: float64

print(s.round(2))
# 0    0.00
# 1    0.02
# 2    0.02
# 3    0.04
# 4    0.04
# 5    2.68
# dtype: float64

print(Decimal(2.675))
# 2.67499999999999982236431605997495353221893310546875

print(Decimal('2.675'))
# 2.675

print(Decimal('2.675').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 2.68

print(Decimal('2.675').quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))
# 2.68

print(Decimal('0.5').quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 1

print(Decimal('0.5').quantize(Decimal('0'), rounding=ROUND_HALF_EVEN))
# 0

s = pd.Series([0.5, 1.5, 2.5, 3.5, 4.5])

print(s.map(lambda x: float(Decimal(str(x)).
                            quantize(Decimal('0'), rounding=ROUND_HALF_UP))))
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# dtype: float64

s = pd.Series([0.005, 0.015, 0.025, 0.035, 0.045, 2.675])

print(s.map(lambda x: float(Decimal(str(x))
                            .quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))))
# 0    0.01
# 1    0.02
# 2    0.03
# 3    0.04
# 4    0.05
# 5    2.68
# dtype: float64

s = pd.Series([5, 15, 25, 5.1, 15.1, 25.1])

print(s.map(lambda x: int(Decimal(str(x))
                          .quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))))
# 0    10
# 1    20
# 2    30
# 3    10
# 4    20
# 5    30
# dtype: int64

s = pd.Series([0.005, 0.015, 0.025, 0.035, 0.045, 2.675])

print(s.map(lambda x: float(Decimal(str(x))
                            .quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))))
# 0    0.00
# 1    0.02
# 2    0.02
# 3    0.04
# 4    0.04
# 5    2.68
# dtype: float64
