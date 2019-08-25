from scipy.sparse import csr_matrix, lil_matrix, hstack, vstack

l = [[0, 1, 2],
     [3, 0, 4],
     [0, 0, 0]]

csr = csr_matrix(l)
lil = lil_matrix(l)

print(hstack([csr, lil]).toarray())
# [[0 1 2 0 1 2]
#  [3 0 4 3 0 4]
#  [0 0 0 0 0 0]]

print(type(hstack([csr, lil])))
# <class 'scipy.sparse.coo.coo_matrix'>

print(type(hstack([csr, lil], format='csr')))
# <class 'scipy.sparse.csr.csr_matrix'>

print(vstack([csr, lil]).toarray())
# [[0 1 2]
#  [3 0 4]
#  [0 0 0]
#  [0 1 2]
#  [3 0 4]
#  [0 0 0]]

print(type(vstack([csr, lil])))
# <class 'scipy.sparse.coo.coo_matrix'>

print(type(vstack([csr, lil], format='csr')))
# <class 'scipy.sparse.csr.csr_matrix'>

print(vstack([csr, lil[:2]]).toarray())
# [[0 1 2]
#  [3 0 4]
#  [0 0 0]
#  [0 1 2]
#  [3 0 4]]

# print(hstack([csr, lil[:2]]))
# ValueError: blocks[0,:] has incompatible row dimensions. Got blocks[0,1].shape[0] == 2, expected 3.
