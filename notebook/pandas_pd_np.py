import pandas as pd

print(pd)
# <module 'pandas' from '/usr/local/lib/python3.7/site-packages/pandas/__init__.py'>

print(pd.np)
# <module 'numpy' from '/usr/local/lib/python3.7/site-packages/numpy/__init__.py'>

import numpy as np

print(pd.np is np)
# True

print(pd.np.mean is np.mean)
# True

a = pd.np.arange(12).reshape(3, 4)

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(type(a))
# <class 'numpy.ndarray'>

print(pd.np.pi)
# 3.141592653589793

print(pd.np.e)
# 2.718281828459045
