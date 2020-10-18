import numpy as np

print(np.__version__)
# 1.19.0

print(np.pi)
# 3.141592653589793

print(np.radians(180))
# 3.141592653589793

print(type(np.radians(180)))
# <class 'numpy.float64'>

a = np.array([0, 90, 180])
print(type(a))
# <class 'numpy.ndarray'>

print(np.radians(a))
# [0.         1.57079633 3.14159265]

print(type(np.radians(a)))
# <class 'numpy.ndarray'>

l = [0, 90, 180]
print(type(l))
# <class 'list'>

print(np.radians(l))
# [0.         1.57079633 3.14159265]

print(type(np.radians(l)))
# <class 'numpy.ndarray'>

print(np.radians(a))
# [0.         1.57079633 3.14159265]

print(np.round(np.radians(a)))
# [0. 2. 3.]

print(np.round(np.radians(a), 2))
# [0.   1.57 3.14]

print(np.sin(np.radians(30)))
# 0.49999999999999994

print(np.round(np.sin(np.radians(30)), 1))
# 0.5

print(np.sin(np.radians([0, 30, 90])))
# [0.  0.5 1. ]

print(np.sin(np.radians([0, 30, 90]))[1])
# 0.49999999999999994

np.set_printoptions(precision=20)
print(np.sin(np.radians([0, 30, 90])))
# [0.                  0.49999999999999994 1.                 ]

np.set_printoptions(precision=8)  # reset to default

print(np.radians([0, 90, 180]))
# [0.         1.57079633 3.14159265]

print(np.deg2rad([0, 90, 180]))
# [0.         1.57079633 3.14159265]

print(np.degrees([0, np.pi / 2, np.pi]))
# [  0.  90. 180.]

print(np.rad2deg([0, np.pi / 2, np.pi]))
# [  0.  90. 180.]

print(np.sin(np.radians([0, 30, 90])))
# [0.  0.5 1. ]

print(np.degrees(np.arcsin([0, 0.5, 1])))
# [ 0. 30. 90.]

print(np.cos(np.radians([0, 60, 90])))
# [1.000000e+00 5.000000e-01 6.123234e-17]

print(np.round(np.cos(np.radians([0, 60, 90])), 1))
# [1.  0.5 0. ]

print(np.degrees(np.arccos([0, 0.5, 1])))
# [90. 60.  0.]

print(np.tan(np.radians([0, 45, 90])))
# [0.00000000e+00 1.00000000e+00 1.63312394e+16]

print(np.degrees(np.arctan([0, 1, np.inf])))
# [ 0. 45. 90.]

print(np.degrees(np.arctan([-np.inf, -1, 0, 1, np.inf])))
# [-90. -45.   0.  45.  90.]

print(np.degrees(np.arctan2(-1, 1)))
# -45.0

print(np.degrees(np.arctan2(1, -1)))
# 135.0

print(np.degrees(np.arctan2([0, 1, 1, 1, 0],
                            [0, 1, 0, -1, -1])))
# [  0.  45.  90. 135. 180.]

print(np.degrees(np.arctan2([0, -1, -1, -1, 0],
                            [0, 1, 0, -1, -1])))
# [   0.  -45.  -90. -135.  180.]

print(np.degrees(np.arctan2(0, -1)))
# 180.0

print(np.degrees(np.arctan2(-0.0, -1.0)))
# -180.0

print(np.degrees(np.arctan2(-0, -1)))
# 180.0

print(np.degrees(np.arctan2([0.0, -0.0, 0.0, -0.0],
                            [0.0, 0.0, -0.0, -0.0])))
# [   0.   -0.  180. -180.]

print(np.sin(-0.0))
# -0.0

print(np.arcsin(-0.0))
# -0.0

print(np.tan(-0.0))
# -0.0

print(np.arctan(-0.0))
# -0.0
