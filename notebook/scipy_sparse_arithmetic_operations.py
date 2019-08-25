import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

l = [[0, 1, 2],
     [3, 0, 4],
     [0, 0, 0]]

csr = csr_matrix(l)

print((csr + csr).toarray())
# [[0 2 4]
#  [6 0 8]
#  [0 0 0]]

print(type((csr + csr)))
# <class 'scipy.sparse.csr.csr_matrix'>

print((csr - csr).toarray())
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

print((csr * csr).toarray())
# [[3 0 4]
#  [0 3 6]
#  [0 0 0]]

print((csr.multiply(csr)).toarray())
# [[ 0  1  4]
#  [ 9  0 16]
#  [ 0  0  0]]

print((csr.dot(csr)).toarray())
# [[3 0 4]
#  [0 3 6]
#  [0 0 0]]

print(csr / csr)
# [[nan  1.  1.]
#  [ 1. nan  1.]
#  [nan nan nan]]

print(type(csr / csr))
# <class 'numpy.matrix'>

print(np.array(csr / csr))
# [[nan  1.  1.]
#  [ 1. nan  1.]
#  [nan nan nan]]

print(type(np.array(csr / csr)))
# <class 'numpy.ndarray'>

csr_full = csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(csr_full / csr_full)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

print(type(csr_full / csr_full))
# <class 'numpy.matrix'>

# print(csr + 10)
# NotImplementedError: adding a nonzero scalar to a sparse matrix is not supported

# print(csr - 10)
# NotImplementedError: subtracting a nonzero scalar from a sparse matrix is not supported

# print(csr_full + 10)
# NotImplementedError: adding a nonzero scalar to a sparse matrix is not supported

# print(csr_full - 10)
# NotImplementedError: subtracting a nonzero scalar from a sparse matrix is not supported

print((csr * 10).toarray())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print((csr / 10).toarray())
# [[0.  0.1 0.2]
#  [0.3 0.  0.4]
#  [0.  0.  0. ]]

print((csr ** 2).toarray())
# [[3 0 4]
#  [0 3 6]
#  [0 0 0]]

print((csr ** 3).toarray())
# [[ 0  3  6]
#  [ 9  0 12]
#  [ 0  0  0]]

print((csr * csr * csr).toarray())
# [[ 0  3  6]
#  [ 9  0 12]
#  [ 0  0  0]]

# print((csr ** -1).toarray())
# alueError: exponent must be >= 0

# print((csr ** 0.5).toarray())
# ValueError: exponent must be an integer

csc = csc_matrix(l)
coo = coo_matrix(l)
lil = lil_matrix(l)

print(type(csc + csc))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(csr + csc))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(csc + csr))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(coo + coo))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(lil + lil))
# <class 'scipy.sparse.csr.csr_matrix'>

a = np.array(l)
print(a)
# [[0 1 2]
#  [3 0 4]
#  [0 0 0]]

print(type(a))
# <class 'numpy.ndarray'>

print(a + csr)
# [[0 2 4]
#  [6 0 8]
#  [0 0 0]]

print(type(a + csr))
# <class 'numpy.matrix'>

print(type(csr - a))
# <class 'numpy.matrix'>

# print(type(a / csr))
# TypeError: unsupported operand type(s) for /: 'numpy.ndarray' and 'csr_matrix'

print(csr / a)
# [[nan  1.  1.]
#  [ 1. nan  1.]
#  [nan nan nan]]
# 
# /usr/local/lib/python3.7/site-packages/scipy/sparse/base.py:596: RuntimeWarning: invalid value encountered in true_divide
#   return np.true_divide(self.todense(), other)

print(type(csr / a))
# <class 'numpy.matrix'>
# 
# /usr/local/lib/python3.7/site-packages/scipy/sparse/base.py:596: RuntimeWarning: invalid value encountered in true_divide
#   return np.true_divide(self.todense(), other)

print(csr * a)
# [[3 0 4]
#  [0 3 6]
#  [0 0 0]]

print(type(csr * a))
# <class 'numpy.ndarray'>

print(type(a * csr))
# <class 'numpy.ndarray'>

print(type(csr.dot(a)))
# <class 'numpy.ndarray'>

print(a.dot(csr))
# [[<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]
#  [<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]
#  [<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]]

print(csr.multiply(a))
#   (0, 1)	1
#   (0, 2)	4
#   (1, 0)	9
#   (1, 2)	16

print(type(csr.multiply(a)))
# <class 'scipy.sparse.coo.coo_matrix'>

print(csr.multiply(a).toarray())
# [[ 0  1  4]
#  [ 9  0 16]
#  [ 0  0  0]]

print(np.multiply(a, csr))
# [[<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]
#  [<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]
#  [<3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>
#   <3x3 sparse matrix of type '<class 'numpy.int64'>'
# 	with 4 stored elements in Compressed Sparse Row format>]]
