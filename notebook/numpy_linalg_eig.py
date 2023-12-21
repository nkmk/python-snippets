import numpy as np

print(np.__version__)
# 1.26.2

a = np.array([[8, 1], [4, 5]])
print(a)
# [[8 1]
#  [4 5]]

eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
# [9. 4.]

print(eigenvectors)
# [[ 0.70710678 -0.24253563]
#  [ 0.70710678  0.9701425 ]]

print(a @ eigenvectors[:, 0] == eigenvalues[0] * eigenvectors[:, 0])
# [ True  True]

print(a @ eigenvectors[:, 1] == eigenvalues[1] * eigenvectors[:, 1])
# [ True  True]

print(eigenvalues[np.argmax(eigenvalues)])
# 9.0

print(eigenvectors[:, np.argmax(eigenvalues)])
# [0.70710678 0.70710678]

def get_eigenpairs(a):
    values, vectors = np.linalg.eig(a)
    pairs = []

    for i, val in enumerate(values):
        vec = vectors[:, i] / min(x for x in np.abs(vectors[:, i]) if x != 0)
        pairs.append((val, vec))

    return pairs

for val, vec in get_eigenpairs(a):
    print(f'value: {val}, vector: {vec}')
# value: 9.0, vector: [1. 1.]
# value: 4.0, vector: [-1.  4.]

a_3d = np.array([[1, 1, 2], [0, 2, -1], [0, 0, 3]])
print(a_3d)
# [[ 1  1  2]
#  [ 0  2 -1]
#  [ 0  0  3]]

for val, vec in get_eigenpairs(a_3d):
    print(f'value: {val}, vector: {vec}')
# value: 1.0, vector: [1. 0. 0.]
# value: 2.0, vector: [1. 1. 0.]
# value: 3.0, vector: [ 1. -2.  2.]

a = np.array([[3, 2], [-2, 3]])
print(a)
# [[ 3  2]
#  [-2  3]]

for val, vec in get_eigenpairs(a):
    print(f'value: {val:.1}, vector: {vec}')
# value: (3+2j), vector: [0.-1.j 1.+0.j]
# value: (3-2j), vector: [0.+1.j 1.-0.j]
