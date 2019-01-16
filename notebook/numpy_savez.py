import numpy as np

a1 = np.arange(5)
print(a1)
# [0 1 2 3 4]

a2 = np.arange(5, 10)
print(a2)
# [5 6 7 8 9]

np.savez('data/temp/np_savez', a1, a2)

print(type(np.load('data/temp/np_savez.npz')))
# <class 'numpy.lib.npyio.NpzFile'>

npz = np.load('data/temp/np_savez.npz')

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
