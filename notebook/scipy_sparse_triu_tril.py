from scipy.sparse import csr_matrix, triu, tril

l = [[0, 1, 2],
     [3, 0, 4],
     [5, 6, 7]]

csr = csr_matrix(l)

print(triu(csr).toarray())
# [[0 1 2]
#  [0 0 4]
#  [0 0 7]]

print(type(triu(csr)))
# <class 'scipy.sparse.coo.coo_matrix'>

print(type(triu(csr, format='csr')))
# <class 'scipy.sparse.csr.csr_matrix'>

print(triu(csr, k=1).toarray())
# [[0 1 2]
#  [0 0 4]
#  [0 0 0]]

print(triu(csr, k=-1).toarray())
# [[0 1 2]
#  [3 0 4]
#  [0 6 7]]

print(tril(csr).toarray())
# [[0 0 0]
#  [3 0 0]
#  [5 6 7]]

print(type(tril(csr)))
# <class 'scipy.sparse.coo.coo_matrix'>

print(type(tril(csr, format='csr')))
# <class 'scipy.sparse.csr.csr_matrix'>

print(tril(csr, k=1).toarray())
# [[0 1 0]
#  [3 0 4]
#  [5 6 7]]

print(tril(csr, k=-1).toarray())
# [[0 0 0]
#  [3 0 0]
#  [5 6 0]]
