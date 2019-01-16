import numpy as np

a1 = np.arange(5)
print(a1)
# [0 1 2 3 4]

a2 = np.arange(5, 10)
print(a2)
# [5 6 7 8 9]

np.savez_compressed('data/temp/np_savez_comp', a1, a2)

print(type(np.load('data/temp/np_savez_comp.npz')))
# <class 'numpy.lib.npyio.NpzFile'>

npz_comp = np.load('data/temp/np_savez_comp.npz')

print(npz_comp.files)
# ['arr_0', 'arr_1']

print(npz_comp['arr_0'])
# [0 1 2 3 4]

print(npz_comp['arr_1'])
# [5 6 7 8 9]

np.savez_compressed('data/temp/np_savez_comp_kw', x=a1, y=a2)

npz_comp_kw = np.load('data/temp/np_savez_comp_kw.npz')

print(npz_comp_kw.files)
# ['x', 'y']

print(npz_comp_kw['x'])
# [0 1 2 3 4]

print(npz_comp_kw['y'])
# [5 6 7 8 9]
