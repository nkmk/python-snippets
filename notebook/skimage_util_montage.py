import numpy as np

import skimage.util

a = np.arange(1, 7).reshape(2, 3)
print(a)
# [[1 2 3]
#  [4 5 6]]

b = a * 10
print(b)
# [[10 20 30]
#  [40 50 60]]

c = a * 100
print(c)
# [[100 200 300]
#  [400 500 600]]

m = skimage.util.montage([a, b, c])
print(m)
# [[  1   2   3  10  20  30]
#  [  4   5   6  40  50  60]
#  [100 200 300 129 129 129]
#  [400 500 600 129 129 129]]

print(m.shape)
# (4, 6)

abc = np.array([a, b, c])
print(abc)
# [[[  1   2   3]
#   [  4   5   6]]
# 
#  [[ 10  20  30]
#   [ 40  50  60]]
# 
#  [[100 200 300]
#   [400 500 600]]]

print(abc.shape)
# (3, 2, 3)

print(skimage.util.montage(abc))
# [[  1   2   3  10  20  30]
#  [  4   5   6  40  50  60]
#  [100 200 300 129 129 129]
#  [400 500 600 129 129 129]]

d = a[:, :2]
print(d)
# [[1 2]
#  [4 5]]

# skimage.util.montage([a, b, c, d])
# ValueError: could not broadcast input array from shape (2,3) into shape (2)

print(np.mean(np.array([a, b, c])))
# 129.5

print(skimage.util.montage([a, b, c], fill=0))
# [[  1   2   3  10  20  30]
#  [  4   5   6  40  50  60]
#  [100 200 300   0   0   0]
#  [400 500 600   0   0   0]]

print(skimage.util.montage([a, b, c], grid_shape=(1, 3)))
# [[  1   2   3  10  20  30 100 200 300]
#  [  4   5   6  40  50  60 400 500 600]]

print(skimage.util.montage([a, b, c], grid_shape=(3, 1)))
# [[  1   2   3]
#  [  4   5   6]
#  [ 10  20  30]
#  [ 40  50  60]
#  [100 200 300]
#  [400 500 600]]

# print(skimage.util.montage([a, b, c], grid_shape=(1, 2)))
# IndexError: list index out of range

print(skimage.util.montage([a, b, c], grid_shape=(2, 3)))
# [[  1   2   3  10  20  30 100 200 300]
#  [  4   5   6  40  50  60 400 500 600]
#  [129 129 129 129 129 129 129 129 129]
#  [129 129 129 129 129 129 129 129 129]]

print(skimage.util.montage([a, b, c], grid_shape=(2, 3), fill=0))
# [[  1   2   3  10  20  30 100 200 300]
#  [  4   5   6  40  50  60 400 500 600]
#  [  0   0   0   0   0   0   0   0   0]
#  [  0   0   0   0   0   0   0   0   0]]

print(skimage.util.montage([a, b, c], padding_width=1))
# [[129 129 129 129 129 129 129 129 129]
#  [129   1   2   3 129  10  20  30 129]
#  [129   4   5   6 129  40  50  60 129]
#  [129 129 129 129 129 129 129 129 129]
#  [129 100 200 300 129 129 129 129 129]
#  [129 400 500 600 129 129 129 129 129]
#  [129 129 129 129 129 129 129 129 129]]

print(skimage.util.montage([a, b, c], padding_width=1, fill=0))
# [[  0   0   0   0   0   0   0   0   0]
#  [  0   1   2   3   0  10  20  30   0]
#  [  0   4   5   6   0  40  50  60   0]
#  [  0   0   0   0   0   0   0   0   0]
#  [  0 100 200 300   0   0   0   0   0]
#  [  0 400 500 600   0   0   0   0   0]
#  [  0   0   0   0   0   0   0   0   0]]
