import numpy as np

print(np.__version__)
# 1.26.1

a = np.arange(6, dtype=np.int8).reshape(1, 2, 3)
print(a)
# [[[0 1 2]
#   [3 4 5]]]

print(a.shape)
# (1, 2, 3)

print(a.dtype)
# int8

np.save('data/temp/np_save', a)

a_load = np.load('data/temp/np_save.npy')
print(a_load)
# [[[0 1 2]
#   [3 4 5]]]

print(a_load.shape)
# (1, 2, 3)

print(a_load.dtype)
# int8

a1 = np.arange(5)
print(a1)
# [0 1 2 3 4]

a2 = np.arange(5, 10)
print(a2)
# [5 6 7 8 9]

np.savez('data/temp/np_savez', a1, a2)

npz = np.load('data/temp/np_savez.npz')
print(type(npz))
# <class 'numpy.lib.npyio.NpzFile'>

print(npz.files)
# ['arr_0', 'arr_1']

print(npz['arr_0'])
# [0 1 2 3 4]

print(npz['arr_1'])
# [5 6 7 8 9]

np.savez('data/temp/np_savez_kw', x=a1, y=a2)

npz_kw = np.load('data/temp/np_savez_kw.npz')
print(npz_kw.files)
# ['x', 'y']

print(npz_kw['x'])
# [0 1 2 3 4]

print(npz_kw['y'])
# [5 6 7 8 9]

np.savez('data/temp/np_savez_kw2', a1, y=a2)

npz_kw2 = np.load('data/temp/np_savez_kw2.npz')
print(npz_kw2.files)
# ['y', 'arr_0']

print(npz_kw2['arr_0'])
# [0 1 2 3 4]

print(npz_kw2['y'])
# [5 6 7 8 9]

np.savez_compressed('data/temp/np_savez_comp', a1, a2)

npz_comp = np.load('data/temp/np_savez_comp.npz')
print(type(npz_comp))
# <class 'numpy.lib.npyio.NpzFile'>

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
