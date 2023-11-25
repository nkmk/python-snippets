import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([[10.0, 10.1, 10.9], [-10.0, -10.1, -10.9]])
print(a)
# [[ 10.   10.1  10.9]
#  [-10.  -10.1 -10.9]]

print(np.floor(a))
# [[ 10.  10.  10.]
#  [-10. -11. -11.]]

print(np.floor(a).dtype)
# float64

print(np.floor(a).astype(int))
# [[ 10  10  10]
#  [-10 -11 -11]]

print(np.floor(10.1))
# 10.0

print(np.trunc(a))
# [[ 10.  10.  10.]
#  [-10. -10. -10.]]

print(np.fix(a))
# [[ 10.  10.  10.]
#  [-10. -10. -10.]]

print(a.astype(int))
# [[ 10  10  10]
#  [-10 -10 -10]]

print(np.ceil(a))
# [[ 10.  11.  11.]
#  [-10. -10. -10.]]

print(np.copysign(np.ceil(np.abs(a)), a))
# [[ 10.  11.  11.]
#  [-10. -11. -11.]]
