import numpy as np

print(np.empty(3))
# [ -3.10503618e+231  -3.10503618e+231  -3.10503618e+231]

print(np.empty((2, 3)))
# [[ -3.10503618e+231   2.68677888e+154   6.92663118e-310]
#  [  1.06099790e-313   6.92663119e-310   4.17211958e-309]]

print(np.empty(3).dtype)
# float64

print(np.empty(3, dtype=np.int))
# [-1152921504606846976 -1152921504606846976 -1152921504606846974]

print(np.empty(3, dtype=np.int).dtype)
# int64

a_int = np.arange(6).reshape((2,3))
print(a_int)
# [[0 1 2]
#  [3 4 5]]

print(np.empty_like(a_int))
# [[8070450532247928832 6917537789928580555     140196575903747]
#  [        21474836480     140196576086528     844446404968448]]

a_float = np.arange(6).reshape((2,3)) / 10
print(a_float)
# [[ 0.   0.1  0.2]
#  [ 0.3  0.4  0.5]]

print(np.empty_like(a_float))
# [[  0.00000000e+000   4.94065646e-324   9.88131292e-324]
#  [  1.48219694e-323   1.97626258e-323   2.47032823e-323]]

print(np.empty_like(a_float, dtype=np.int))
# [[0 1 2]
#  [3 4 5]]
