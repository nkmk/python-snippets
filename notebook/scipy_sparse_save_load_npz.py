import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, save_npz, load_npz

l = [[0, 1, 2],
     [3, 0, 4],
     [0, 0, 0]]

csr = csr_matrix(l)
csc = csc_matrix(l)

save_npz('data/temp/csr.npz', csr)
save_npz('data/temp/csc.npz', csc)

csr_ = load_npz('data/temp/csr.npz')
print(csr_.toarray())
# [[0 1 2]
#  [3 0 4]
#  [0 0 0]]

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

csc_ = load_npz('data/temp/csc.npz')
print(csc_.toarray())
# [[0 1 2]
#  [3 0 4]
#  [0 0 0]]

print(type(csc))
# <class 'scipy.sparse.csc.csc_matrix'>

lil = lil_matrix(l)

# save_npz('data/temp/lil.npz', lil)
# NotImplementedError: Save is not implemented for sparse matrix of format lil.

npz = np.load('data/temp/csr.npz')

print(npz.files)
# ['indices', 'indptr', 'format', 'shape', 'data']

print(npz['data'])
# [1 2 3 4]

print(npz['indices'])
# [1 2 0 2]

print(npz['indptr'])
# [0 2 4 4]

print(npz['format'])
# b'csr'

print(npz['shape'])
# [3 3]
