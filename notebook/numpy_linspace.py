import numpy as np

print(np.__version__)
# 1.26.1

print(np.linspace(0, 10, 3))
# [ 0.  5. 10.]

print(np.linspace(0, 10, 4))
# [ 0.          3.33333333  6.66666667 10.        ]

print(np.linspace(0, 10, 5))
# [ 0.   2.5  5.   7.5 10. ]

print(np.linspace(10, 0, 5))
# [10.   7.5  5.   2.5  0. ]

a = np.linspace(0, 10, 3)
print(a)
# [ 0.  5. 10.]

print(a.dtype)
# float64

a_int = np.linspace(0, 10, 3, dtype=int)
print(a_int)
# [ 0  5 10]

print(a_int.dtype)
# int64

print(np.linspace(0, 10, 5))
# [ 0.   2.5  5.   7.5 10. ]

print(np.linspace(0, 10, 5, endpoint=False))
# [0. 2. 4. 6. 8.]

result = np.linspace(0, 10, 5, retstep=True)
print(result)
# (array([ 0. ,  2.5,  5. ,  7.5, 10. ]), 2.5)

print(type(result))
# <class 'tuple'>

print(result[0])
# [ 0.   2.5  5.   7.5 10. ]

print(result[1])
# 2.5

print(np.linspace(0, 10, 5, retstep=True)[1])
# 2.5

print(np.linspace(0, 10, 5, retstep=True, endpoint=False)[1])
# 2.0

print(np.linspace(0, 10, 5))
# [ 0.   2.5  5.   7.5 10. ]

print(np.linspace(10, 0, 5))
# [10.   7.5  5.   2.5  0. ]

print(np.linspace(0, 10, 5)[::-1])
# [10.   7.5  5.   2.5  0. ]

print(np.flip(np.linspace(0, 10, 5)))
# [10.   7.5  5.   2.5  0. ]

print(np.linspace(0, 10, 5, endpoint=False))
# [0. 2. 4. 6. 8.]

print(np.linspace(10, 0, 5, endpoint=False))
# [10.  8.  6.  4.  2.]

print(np.linspace(0, 10, 5, endpoint=False)[::-1])
# [8. 6. 4. 2. 0.]

print(np.flip(np.linspace(0, 10, 5, endpoint=False)))
# [8. 6. 4. 2. 0.]

print(np.linspace(0, 10, 12).reshape(3, 4))
# [[ 0.          0.90909091  1.81818182  2.72727273]
#  [ 3.63636364  4.54545455  5.45454545  6.36363636]
#  [ 7.27272727  8.18181818  9.09090909 10.        ]]

print(np.linspace(0, 10, 24).reshape(2, 3, 4))
# [[[ 0.          0.43478261  0.86956522  1.30434783]
#   [ 1.73913043  2.17391304  2.60869565  3.04347826]
#   [ 3.47826087  3.91304348  4.34782609  4.7826087 ]]
# 
#  [[ 5.2173913   5.65217391  6.08695652  6.52173913]
#   [ 6.95652174  7.39130435  7.82608696  8.26086957]
#   [ 8.69565217  9.13043478  9.56521739 10.        ]]]
