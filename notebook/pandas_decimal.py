from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR, ROUND_HALF_EVEN

import pandas as pd

print(pd.__version__)
# 2.1.2

s = pd.Series([0.123, 0.456, 0.789])
print(s)
# 0    0.123
# 1    0.456
# 2    0.789
# dtype: float64

s_decimal = s.astype(str).map(Decimal)
print(s_decimal)
# 0    0.123
# 1    0.456
# 2    0.789
# dtype: object

print(type(s_decimal[0]))
# <class 'decimal.Decimal'>

print(s.map(Decimal))
# 0    0.12299999999999999822364316059974953532218933...
# 1    0.45600000000000001643130076445231679826974868...
# 2    0.78900000000000003463895836830488406121730804...
# dtype: object

print(s_decimal.map(lambda x: x.quantize(Decimal('0.1'), ROUND_HALF_UP)))
# 0    0.1
# 1    0.5
# 2    0.8
# dtype: object

print(s_decimal.map(lambda x: x.quantize(Decimal('0.01'), ROUND_FLOOR)))
# 0    0.12
# 1    0.45
# 2    0.78
# dtype: object

print(s_decimal.astype(float))
# 0    0.123
# 1    0.456
# 2    0.789
# dtype: float64

print(s_decimal.astype(float).map(Decimal))
# 0    0.12299999999999999822364316059974953532218933...
# 1    0.45600000000000001643130076445231679826974868...
# 2    0.78900000000000003463895836830488406121730804...
# dtype: object
