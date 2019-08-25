from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

l = [[0, 10, 20],
     [30, 0, 40],
     [0, 0, 50]]

data = [10, 20, 30, 40, 50]
row = [0, 0, 1, 1, 2]
col = [1, 2, 0, 2, 2]

csr = csr_matrix(l)
print(csr)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30
#   (1, 2)	40
#   (2, 2)	50

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

print(csr.data)
# [10 20 30 40 50]

print(csr.indices)
# [1 2 0 2 2]

print(csr.indptr)
# [0 2 4 5]

csc = csc_matrix(l)
print(csc)
#   (1, 0)	30
#   (0, 1)	10
#   (0, 2)	20
#   (1, 2)	40
#   (2, 2)	50

print(type(csc))
# <class 'scipy.sparse.csc.csc_matrix'>

print(csc.data)
# [30 10 20 40 50]

print(csc.indices)
# [1 0 0 1 2]

print(csc.indptr)
# [0 1 2 5]

coo = coo_matrix(l)
print(coo)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30
#   (1, 2)	40
#   (2, 2)	50

print(type(coo))
# <class 'scipy.sparse.coo.coo_matrix'>

print(coo.data)
# [10 20 30 40 50]

print(coo.row)
# [0 0 1 1 2]

print(coo.col)
# [1 2 0 2 2]

lil = lil_matrix(l)
print(lil)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30
#   (1, 2)	40
#   (2, 2)	50

print(type(lil))
# <class 'scipy.sparse.lil.lil_matrix'>

print(lil.data)
# [list([10, 20]) list([30, 40]) list([50])]

print(lil.rows)
# [list([1, 2]) list([0, 2]) list([2])]
