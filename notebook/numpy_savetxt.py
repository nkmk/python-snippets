import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

np.savetxt('data/temp/np_savetxt.txt', a)

with open('data/temp/np_savetxt.txt') as f:
    print(f.read())
# 0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00
# 3.000000000000000000e+00 4.000000000000000000e+00 5.000000000000000000e+00
# 

np.savetxt('data/temp/np_savetxt_5e.txt', a, fmt='%.5e')

with open('data/temp/np_savetxt_5e.txt') as f:
    print(f.read())
# 0.00000e+00 1.00000e+00 2.00000e+00
# 3.00000e+00 4.00000e+00 5.00000e+00
# 

print(np.loadtxt('data/temp/np_savetxt.txt'))
# [[0. 1. 2.]
#  [3. 4. 5.]]

np.savetxt('data/temp/np_savetxt_5f.txt', a, fmt='%.5f')

with open('data/temp/np_savetxt_5f.txt') as f:
    print(f.read())
# 0.00000 1.00000 2.00000
# 3.00000 4.00000 5.00000
# 

np.savetxt('data/temp/np_savetxt_d.txt', a, fmt='%d')

with open('data/temp/np_savetxt_d.txt') as f:
    print(f.read())
# 0 1 2
# 3 4 5
# 

print(a * 10)
# [[ 0 10 20]
#  [30 40 50]]

np.savetxt('data/temp/np_savetxt_x.txt', a * 10, fmt='%04x')

with open('data/temp/np_savetxt_x.txt') as f:
    print(f.read())
# 0000 000a 0014
# 001e 0028 0032
# 

np.savetxt('data/temp/np_savetxt.csv', a, delimiter=',', fmt='%d')

with open('data/temp/np_savetxt.csv') as f:
    print(f.read())
# 0,1,2
# 3,4,5
# 

np.savetxt('data/temp/np_savetxt.tsv', a, delimiter='\t', fmt='%d')

with open('data/temp/np_savetxt.tsv') as f:
    print(f.read())
# 0	1	2
# 3	4	5
# 

a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# np.savetxt('data/temp/np_savetxt_3d.txt', a_3d)
# ValueError: Expected 1D or 2D array, got 3D array instead
