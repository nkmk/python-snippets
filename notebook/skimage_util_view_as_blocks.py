import numpy as np

import skimage.util

a = np.arange(24).reshape(4, 6)
print(a)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

blocks = skimage.util.view_as_blocks(a, (2, 3))
print(blocks)
# [[[[ 0  1  2]
#    [ 6  7  8]]
# 
#   [[ 3  4  5]
#    [ 9 10 11]]]
# 
# 
#  [[[12 13 14]
#    [18 19 20]]
# 
#   [[15 16 17]
#    [21 22 23]]]]

print(type(blocks))
# <class 'numpy.ndarray'>

print(blocks.shape)
# (2, 2, 2, 3)

print(blocks[0, 0])
# [[0 1 2]
#  [6 7 8]]

print(blocks[0, 1])
# [[ 3  4  5]
#  [ 9 10 11]]

print(blocks[1, 0])
# [[12 13 14]
#  [18 19 20]]

print(blocks[1, 1])
# [[15 16 17]
#  [21 22 23]]

# blocks = skimage.util.view_as_blocks(a, (2, 4))
# ValueError: 'block_shape' is not compatible with 'arr_in'

print(np.shares_memory(a, blocks))
# True

a[0, 0] = 100

print(blocks[0, 0])
# [[100   1   2]
#  [  6   7   8]]

a = np.arange(24).reshape(4, 6)
blocks_copy = skimage.util.view_as_blocks(a, (2, 3)).copy()

print(np.shares_memory(a, blocks_copy))
# False

a[0, 0] = 100

print(blocks_copy[0, 0])
# [[0 1 2]
#  [6 7 8]]

blocks_copy2 = skimage.util.view_as_blocks(a.copy(), (2, 3))

print(np.shares_memory(a, blocks_copy2))
# False
