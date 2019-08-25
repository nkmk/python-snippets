from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

l = [[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 3, 0],
     [0, 0, 0, 4]]

csr = csr_matrix(l)
csc = csc_matrix(l)
coo = coo_matrix(l)
lil = lil_matrix(l)

print(csr.getrow(0))
#   (0, 0)	1

print(type(csr.getrow(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

print(csr.getrow(0).shape)
# (1, 4)

print(csr.getrow(0).toarray())
# [[1 0 0 0]]

print(type(csc.getrow(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(coo.getrow(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(lil.getrow(0)))
# <class 'scipy.sparse.lil.lil_matrix'>

print(csr.getcol(0))
#   (0, 0)	1

print(type(csr.getcol(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

print(csr.getcol(0).shape)
# (4, 1)

print(csr.getcol(0).toarray())
# [[1]
#  [0]
#  [0]
#  [0]]

print(type(csc.getcol(0)))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(coo.getcol(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(lil.getcol(0)))
# <class 'scipy.sparse.csr.csr_matrix'>

lil_row = lil.getrow(0)

lil_row[0, 0] = 100

print(lil.toarray())
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

print(lil_row.toarray())
# [[100   0   0   0]]
