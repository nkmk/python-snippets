import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.ravel('F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(np.ravel(a, 'F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(a.flatten('F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(a.reshape(-1, order='F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(np.reshape(a, -1, order='F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

np.info(a)
# class:  ndarray
# shape:  (3, 4)
# strides:  (32, 8)
# itemsize:  8
# aligned:  True
# contiguous:  True
# fortran:  False
# data pointer: 0x7fe081640f90
# byteorder:  little
# byteswap:  False
# type: int64

print(a.ravel('C'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.ravel('F'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(a.ravel('A'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.ravel('K'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

np.info(a.T)
# class:  ndarray
# shape:  (4, 3)
# strides:  (8, 32)
# itemsize:  8
# aligned:  True
# contiguous:  False
# fortran:  True
# data pointer: 0x7fe081640f90
# byteorder:  little
# byteswap:  False
# type: int64

print(a.T.ravel('C'))
# [ 0  4  8  1  5  9  2  6 10  3  7 11]

print(a.T.ravel('F'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.T.ravel('A'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.T.ravel('K'))
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(a.T[::-1])
# [[ 3  7 11]
#  [ 2  6 10]
#  [ 1  5  9]
#  [ 0  4  8]]

np.info(a.T[::-1])
# class:  ndarray
# shape:  (4, 3)
# strides:  (-8, 32)
# itemsize:  8
# aligned:  True
# contiguous:  False
# fortran:  False
# data pointer: 0x7fe081640fa8
# byteorder:  little
# byteswap:  False
# type: int64

print(a.T[::-1].ravel('C'))
# [ 3  7 11  2  6 10  1  5  9  0  4  8]

print(a.T[::-1].ravel('F'))
# [ 3  2  1  0  7  6  5  4 11 10  9  8]

print(a.T[::-1].ravel('A'))
# [ 3  7 11  2  6 10  1  5  9  0  4  8]

print(a.T[::-1].ravel('K'))
# [ 3  2  1  0  7  6  5  4 11 10  9  8]
