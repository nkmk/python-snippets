import numpy as np

def calc_indptr(n, data, row, column, tocsr=True):
    if tocsr:
        Ai, Aj = row, column
    else:
        Ai, Aj = column, row

    indptr = np.zeros(n + 1, dtype=int)
    indices = np.zeros_like(Aj)
    data_ = np.zeros_like(data)
    
    for a in Ai:
        indptr[a + 1] += 1
    
    indptr = indptr.cumsum()
    
    for i, j, d in zip(Ai, Aj, data):
        dest = indptr[i]
        indices[dest] = j
        data_[dest] = d
        indptr[i] += 1
    
    indptr[-1] = 0
        
    return data_, indices, np.roll(indptr, 1)

print(calc_indptr(3, [10, 20, 30, 40], [0, 0, 1, 1], [1, 2, 0, 2]))
# (array([10, 20, 30, 40]), array([1, 2, 0, 2]), array([0, 2, 4, 4]))

print(calc_indptr(3, [10, 20, 30, 40], [0, 0, 1, 1], [1, 2, 0, 2], False))
# (array([30, 10, 20, 40]), array([1, 0, 0, 1]), array([0, 1, 2, 4]))
