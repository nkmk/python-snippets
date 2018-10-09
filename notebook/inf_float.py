f_inf = float('inf')

print(f_inf)
# inf

print(type(f_inf))
# <class 'float'>

f_inf_minus = -float('inf')

print(f_inf_minus)
# -inf

print(type(f_inf_minus))
# <class 'float'>

# print(int(f_inf))
# OverflowError: cannot convert float infinity to integer

print(str(f_inf))
# inf

print(type(str(f_inf)))
# <class 'str'>

print(float('inf'))
# inf

print(float('infinity'))
# inf

print(float('INF'))
# inf

print(float('INFinity'))
# inf

import sys

f_inf_num = sys.float_info.max * 2

print(f_inf_num)
# inf
