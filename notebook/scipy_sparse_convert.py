from scipy.sparse import csr_matrix, lil_matrix

l = [[0, 10, 20],
     [30, 0, 0],
     [0, 0, 0]]

csr = csr_matrix(l)
print(csr)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

lil = csr.tolil()
print(lil)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30

print(type(lil))
# <class 'scipy.sparse.lil.lil_matrix'>

lil = lil_matrix(csr)
print(lil)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30

print(type(lil))
# <class 'scipy.sparse.lil.lil_matrix'>

lil[0, 0] = 100

print(lil.toarray())
# [[100  10  20]
#  [ 30   0   0]
#  [  0   0   0]]

print(csr.toarray())
# [[ 0 10 20]
#  [30  0  0]
#  [ 0  0  0]]

lil2 = lil_matrix(lil)
print(lil2.toarray())
# [[100  10  20]
#  [ 30   0   0]
#  [  0   0   0]]

lil[0, 0] = 0

print(lil2.toarray())
# [[ 0 10 20]
#  [30  0  0]
#  [ 0  0  0]]

lil2_copy = lil_matrix(lil, copy=True)
print(lil2_copy.toarray())
# [[ 0 10 20]
#  [30  0  0]
#  [ 0  0  0]]

lil[0, 0] = 100

print(lil2_copy.toarray())
# [[ 0 10 20]
#  [30  0  0]
#  [ 0  0  0]]
