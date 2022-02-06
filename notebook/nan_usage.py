import math

import numpy as np
import pandas as pd

print(float('nan'))
# nan

print(type(float('nan')))
# <class 'float'>

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

df = pd.read_csv('data/src/sample_pandas_normal_nan.csv')[:3]
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN

print(float('nan'))
# nan

print(float('NaN'))
# nan

print(float('NAN'))
# nan

print(math.nan)
# nan

print(np.nan)
# nan

print(np.NaN)
# nan

print(np.NAN)
# nan

print(math.isnan(float('nan')))
# True

print(math.isnan(math.nan))
# True

print(math.isnan(np.nan))
# True

print(np.isnan(float('nan')))
# True

print(np.isnan([float('nan'), math.nan, np.nan, 0]))
# [ True  True  True False]

print(10 < float('nan'))
# False

print(10 > float('nan'))
# False

print(10 == float('nan'))
# False

print(10 != float('nan'))
# True

print(float('nan') == float('nan'))
# False

print(float('nan') != float('nan'))
# True

print(bool(float('nan')))
# True

x = float('nan')

if math.isnan(x):
    print('This is nan.')
else:
    print('This is not nan.')
# This is nan.

x = 100

if math.isnan(x):
    print('This is nan.')
else:
    print('This is not nan.')
# This is not nan.

l = [float('nan'), 0, 1, 2]
print(l)
# [nan, 0, 1, 2]

print([x for x in l if not math.isnan(x)])
# [0, 1, 2]

print([-100 if math.isnan(x) else x for x in l])
# [-100, 0, 1, 2]

print(float('nan') + 100)
# nan

print(float('nan') - 100)
# nan

print(float('nan') - 100)
# nan

print(float('nan') / 100)
# nan

print(float('nan') ** 100)
# nan
