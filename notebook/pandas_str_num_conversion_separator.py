import pandas as pd

s_sep = pd.Series(['1,000,000', '1,000', '1'])
print(s_sep)
# 0    1,000,000
# 1        1,000
# 2            1
# dtype: object

# print(s_sep.astype(int))
# ValueError: invalid literal for int() with base 10: '1,000,000'

print(s_sep.str.replace(',', '').astype(int))
# 0    1000000
# 1       1000
# 2          1
# dtype: int64

print(s_sep.str.replace(',', '').astype(float))
# 0    1000000.0
# 1       1000.0
# 2          1.0
# dtype: float64
