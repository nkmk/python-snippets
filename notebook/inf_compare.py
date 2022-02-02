import math
import numpy as np

print(1e1000)
# inf

print(1e100)
# 1e+100

print(1e1000 == float('inf'))
# True

print(1e100 == float('inf'))
# False

print(float('inf') == math.inf == np.inf)
# True

print(1e1000 == math.inf)
# True

print(1e100 == math.inf)
# False

print(float('inf') == float('inf') * 100)
# True

print(math.isinf(1e1000))
# True

print(math.isinf(1e100))
# False

print(math.isinf(-1e1000))
# True

a = np.array([1, np.inf, -np.inf])
print(a)
# [  1.  inf -inf]

print(np.isinf(a))
# [False  True  True]

print(np.isposinf(a))
# [False  True False]

print(np.isneginf(a))
# [False False  True]

print(np.isfinite(a))
# [ True False False]

print(np.isinf(1e1000))
# True

print(np.nan_to_num(a))
# [ 1.00000000e+000  1.79769313e+308 -1.79769313e+308]

print(np.nan_to_num(a, posinf=1e100, neginf=-1e100))
# [ 1.e+000  1.e+100 -1.e+100]

np.nan_to_num(a, copy=False)
print(a)
# [ 1.00000000e+000  1.79769313e+308 -1.79769313e+308]

import sys

print(sys.float_info.max)
# 1.7976931348623157e+308

print(float('inf') > sys.float_info.max)
# True

print(-float('inf') < -sys.float_info.max)
# True

print(float('nan'))
# nan

print(type(float('nan')))
# <class 'float'>

print(float('inf') > float('nan'))
# False

print(float('inf') < float('nan'))
# False

print(float('inf') == float('nan'))
# False

print(float('inf') > 100)
# True

large_int = int(sys.float_info.max) * 10

print(large_int)
# 1797693134862315708145274237317043567980705675258449965989174768031572607800285387605895586327668781715404589535143824642343213268894641827684675467035375169860499105765512820762454900903893289440758685084551339423045832369032229481658085593321233482747978262041447231687381771809192998812504040261841248583680

print(type(large_int))
# <class 'int'>

print(large_int > sys.float_info.max)
# True

print(float('inf') > large_int)
# True

print(float(10**308))
# 1e+308

# print(float(10**309))
# OverflowError: int too large to convert to float
