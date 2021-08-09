import scipy.stats
import numpy as np
import pandas as pd

import scipy

print(scipy.__version__)
# 1.7.1

a = np.array([2**n for n in range(10)])
print(a)
# [  1   2   4   8  16  32  64 128 256 512]

print(type(a))
# <class 'numpy.ndarray'>

print(a.mean())
# 102.3

print(np.mean(a))
# 102.3

print(scipy.stats.trim_mean(a, 0.1))
# 63.75

print(scipy.stats.trim_mean(a, 0.2))
# 42.0

print(scipy.stats.trimboth(a, 0.1))
# [  2   8   4  16  32  64 128 256]

print(scipy.stats.trimboth(a, 0.2))
# [  4  16   8  32  64 128]

print(scipy.stats.trimboth(a, 0.19))
# [  2   8   4  16  32  64 128 256]

print(scipy.stats.trim_mean(a, 0.19))
# 63.75

a_unsorted = np.array([100, 1000, 0, 10000, 10])
print(a_unsorted)
# [  100  1000     0 10000    10]

print(scipy.stats.trimboth(a_unsorted, 0.2))
# [  10  100 1000]

print(scipy.stats.trim_mean(a_unsorted, 0.2))
# 370.0

print(a_unsorted[1:-1])
# [ 1000     0 10000]

print(a_unsorted[1:-1].mean())
# 3666.6666666666665

a_2d = np.array([2**n for n in range(16)]).reshape(4, 4)
print(a_2d)
# [[    1     2     4     8]
#  [   16    32    64   128]
#  [  256   512  1024  2048]
#  [ 4096  8192 16384 32768]]

print(scipy.stats.trimboth(a_2d, 0.25))
# [[  16   32   64  128]
#  [ 256  512 1024 2048]]

print(scipy.stats.trim_mean(a_2d, 0.25))
# [ 136.  272.  544. 1088.]

print(scipy.stats.trimboth(a_2d, 0.25, axis=1))
# [[    2     4]
#  [   32    64]
#  [  512  1024]
#  [ 8192 16384]]

print(scipy.stats.trim_mean(a_2d, 0.25, axis=1))
# [3.0000e+00 4.8000e+01 7.6800e+02 1.2288e+04]

print(scipy.stats.trimboth(a_2d, 0.25, axis=None))
# [  16   32   64  128  512  256 1024 2048]

print(scipy.stats.trim_mean(a_2d, 0.25, axis=None))
# 510.0

print(a)
# [  1   2   4   8  16  32  64 128 256 512]

print(scipy.stats.tmean(a, (4, 32)))
# 15.0

print(scipy.stats.tmean(a, (None, 32)))
# 10.5

print(scipy.stats.tmean(a, (4, 32), (False, False)))
# 12.0

print(a_2d)
# [[    1     2     4     8]
#  [   16    32    64   128]
#  [  256   512  1024  2048]
#  [ 4096  8192 16384 32768]]

print(scipy.stats.tmean(a_2d, (16, 2048)))
# 510.0

print(scipy.stats.tmean(a_2d, (16, 2048), axis=0))
# 510.0

# print(scipy.stats.tmean(a_2d, (16, 2048), axis=1))
# AxisError: axis 1 is out of bounds for array of dimension 1

for i in range(a_2d.shape[1]):
    print(scipy.stats.tmean(a_2d[:, i], (16, 2048)))
# 136.0
# 272.0
# 544.0
# 1088.0

df = pd.DataFrame(a_2d,
                  index=['R1', 'R2', 'R3', 'R4'],
                  columns=['C1', 'C2', 'C3', 'C4'])
print(df)
#       C1    C2     C3     C4
# R1     1     2      4      8
# R2    16    32     64    128
# R3   256   512   1024   2048
# R4  4096  8192  16384  32768

print(type(df['C1']))
# <class 'pandas.core.series.Series'>

print(scipy.stats.trim_mean(df['C1'], 0.25))
# 136.0

print(scipy.stats.trimboth(df['C1'], 0.25))
# [ 16 256]

print(type(scipy.stats.trimboth(df['C1'], 0.25)))
# <class 'numpy.ndarray'>

print(scipy.stats.trim_mean(df, 0.25))
# [ 136.  272.  544. 1088.]

print(type(scipy.stats.trim_mean(df, 0.25)))
# <class 'numpy.ndarray'>

print(scipy.stats.trimboth(df, 0.25))
# [[  16   32   64  128]
#  [ 256  512 1024 2048]]

print(type(scipy.stats.trimboth(df, 0.25)))
# <class 'numpy.ndarray'>

print(scipy.stats.trim_mean(df, 0.25, axis=1))
# [3.0000e+00 4.8000e+01 7.6800e+02 1.2288e+04]

print(scipy.stats.trim_mean(df, 0.25, axis=None))
# 510.0

s_tm = pd.Series(scipy.stats.trim_mean(df, 0.25),
                 index=df.columns)

print(s_tm)
# C1     136.0
# C2     272.0
# C3     544.0
# C4    1088.0
# dtype: float64

print(scipy.stats.tmean(df, (16, 2048)))
# 510.0

print(scipy.stats.tmean(df['C1'], (16, 2048)))
# 136.0

for col in df:
    print(col, scipy.stats.tmean(df[col], (16, 2048)))
# C1 136.0
# C2 272.0
# C3 544.0
# C4 1088.0

df['C5'] = ['A', 'B', 'C', 'D']
print(df)
#       C1    C2     C3     C4 C5
# R1     1     2      4      8  A
# R2    16    32     64    128  B
# R3   256   512   1024   2048  C
# R4  4096  8192  16384  32768  D

# print(scipy.stats.trim_mean(df, 0.25))
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

print(df.select_dtypes(include='number'))
#       C1    C2     C3     C4
# R1     1     2      4      8
# R2    16    32     64    128
# R3   256   512   1024   2048
# R4  4096  8192  16384  32768

print(scipy.stats.trim_mean(df.select_dtypes(include='number'), 0.25))
# [ 136.  272.  544. 1088.]
