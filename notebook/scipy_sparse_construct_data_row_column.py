from scipy.sparse import csr_matrix, csc_matrix, coo_matrix

data = [10, 20, 30, 40]
row = [0, 0, 1, 1]
col = [1, 2, 0, 2]

print(csr_matrix((data, (row, col))).toarray())
# [[ 0 10 20]
#  [30  0 40]]

print(csr_matrix((data, (row, col)), shape=(3, 3)).toarray())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print(csr_matrix((data, (row, col)), shape=(4, 4)).toarray())
# [[ 0 10 20  0]
#  [30  0 40  0]
#  [ 0  0  0  0]
#  [ 0  0  0  0]]

data = [10, 20, 30, 40]
row = [0, 0, 1, 1]
col = [1, 2, 2, 2]

print(csr_matrix((data, (row, col))))
#   (0, 1)	10
#   (0, 2)	20
#   (1, 2)	70

print(csc_matrix((data, (row, col))))
#   (0, 1)	10
#   (0, 2)	20
#   (1, 2)	70

print(coo_matrix((data, (row, col))))
#   (0, 1)	10
#   (0, 2)	20
#   (1, 2)	30
#   (1, 2)	40

print(coo_matrix((data, (row, col))).tocsr())
#   (0, 1)	10
#   (0, 2)	20
#   (1, 2)	70

print(coo_matrix((data, (row, col))).toarray())
# [[ 0 10 20]
#  [ 0  0 70]]

print(csr_matrix(([10, 20, 30, 40], [1, 2, 0, 2], [0, 2, 4, 4]), shape=(3, 3)).toarray())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print(csc_matrix(([30, 10, 20, 40], [1, 0, 0, 1], [0, 1, 2, 4]), shape=(3, 3)).toarray())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]
