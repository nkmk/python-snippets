import numpy as np

print(np.__version__)
# 1.26.2

a = np.array([[0, 1], [2, 3]])
print(a)
# [[0 1]
#  [2 3]]

print(np.linalg.det(a))
# -2.0
