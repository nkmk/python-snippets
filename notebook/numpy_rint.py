import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([12.3, 45.6, 78.9])

print(np.rint(a))
# [12. 46. 79.]

l = [12.3, 45.6, 78.9]

print(np.rint(l))
# [12. 46. 79.]

print(np.rint(12.3))
# 12.0

print(np.rint(a).dtype)
# float64

print(np.rint([-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]))
# [-4. -2. -2. -0.  0.  2.  2.  4.]
