import numpy as np

arr = np.array([[8, 1], [4, 5]])

w, v = np.linalg.eig(arr)

print(w)
# [9. 4.]

print(v)
# [[ 0.70710678 -0.24253563]
#  [ 0.70710678  0.9701425 ]]

print('value: ', w[0])
print('vector: ', v[:, 0] / v[0, 0])
# value:  9.0
# vector:  [1. 1.]

print(w[np.argmax(w)])
print(v[:, np.argmax(w)])
# 9.0
# [0.70710678 0.70710678]

def get_eigenpairs(arr):
    w, v = np.linalg.eig(arr)
    eigenpairs = []
    
    for i, val in enumerate(w):
        vec = v[:, i] / np.min(np.abs(v[:, i][v[:, i] != 0]))
        eigenpairs.append((val, vec))
        
    return eigenpairs

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 9.0, vector: [1. 1.]
# value: 4.0, vector: [-1.  4.]

arr = np.array([[1, 1, 2], [0, 2, -1], [0, 0, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 1.0, vector: [1. 0. 0.]
# value: 2.0, vector: [1. 1. 0.]
# value: 3.0, vector: [ 1. -2.  2.]

arr = np.array([[3, 2], [-2, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: (3+2.0000000000000004j), vector: [0.-1.j 1.+0.j]
# value: (3-2.0000000000000004j), vector: [0.+1.j 1.-0.j]
