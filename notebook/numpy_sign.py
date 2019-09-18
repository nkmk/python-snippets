import numpy as np

a = np.array([-100, -10, 0, 10, 100])
print(a)
# [-100  -10    0   10  100]

print(np.sign(a))
# [-1 -1  0  1  1]

print(type(np.sign(a)))
# <class 'numpy.ndarray'>

print(np.sign(a).dtype)
# int64

a_float = np.array([-1.23, 0.0, 1.23])
print(a_float)
# [-1.23  0.    1.23]

print(np.sign(a_float))
# [-1.  0.  1.]

print(np.sign(a_float).dtype)
# float64

print(np.sign(100))
# 1

print(type(np.sign(100)))
# <class 'numpy.int64'>

print(np.sign(-1.23))
# -1.0

print(type(np.sign(-1.23)))
# <class 'numpy.float64'>

a_special = np.array([-np.inf, np.inf, np.nan])
print(a_special)
# [-inf  inf  nan]

print(np.sign(a_special))
# [-1.  1. nan]

print(np.sign(a_special).dtype)
# float64

a_complex = np.array([[10 + 10j, -10 + 10j], [10 - 10j, -10 - 10j], [10, -10], [10j, -10j], [0, np.nan], [0j, np.nan * 1j]])
print(a_complex)
# [[ 10.+10.j -10.+10.j]
#  [ 10.-10.j -10.-10.j]
#  [ 10. +0.j -10. +0.j]
#  [  0.+10.j  -0.-10.j]
#  [  0. +0.j  nan +0.j]
#  [  0. +0.j  nan+nanj]]

print(np.sign(a_complex))
# [[ 1.+0.j -1.+0.j]
#  [ 1.+0.j -1.+0.j]
#  [ 1.+0.j -1.+0.j]
#  [ 1.+0.j -1.+0.j]
#  [ 0.+0.j nan+0.j]
#  [ 0.+0.j nan+0.j]]

print(a_complex.real)
# [[ 10. -10.]
#  [ 10. -10.]
#  [ 10. -10.]
#  [  0.  -0.]
#  [  0.  nan]
#  [  0.  nan]]

print(np.sign(a_complex.real))
# [[ 1. -1.]
#  [ 1. -1.]
#  [ 1. -1.]
#  [ 0.  0.]
#  [ 0. nan]
#  [ 0. nan]]

print(a_complex.imag)
# [[ 10.  10.]
#  [-10. -10.]
#  [  0.   0.]
#  [ 10. -10.]
#  [  0.   0.]
#  [  0.  nan]]

print(np.sign(a_complex.imag))
# [[ 1.  1.]
#  [-1. -1.]
#  [ 0.  0.]
#  [ 1. -1.]
#  [ 0.  0.]
#  [ 0. nan]]
