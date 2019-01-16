import numpy as np

a = np.arange(5)
print(a)
# [0 1 2 3 4]

np.save('data/temp/np_save', a)

print(type(np.load('data/temp/np_save.npy')))
# <class 'numpy.ndarray'>

print(np.load('data/temp/np_save.npy'))
# [0 1 2 3 4]

np.save('data/temp/np_save', a.astype('float32'))

b = np.load('data/temp/np_save.npy')

print(b)
# [0. 1. 2. 3. 4.]

print(b.dtype)
# float32
