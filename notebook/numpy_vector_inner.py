import numpy as np

v1 = np.array([0, 1, 2])
v2 = np.array([3, 4, 5])

inner = np.inner(v1, v2)

print(inner)
# 14

inner_dot = np.dot(v1, v2)

print(inner_dot)
# 14

inner_matmul = np.matmul(v1, v2)

print(inner_matmul)
# 14

inner_matmul = v1 @ v2

print(inner_matmul)
# 14
