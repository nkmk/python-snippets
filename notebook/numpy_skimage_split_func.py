import numpy as np

import skimage.io
import skimage.util

img = skimage.io.imread('data/src/lena_square.png')
print(img.shape)
# (512, 512, 3)

def split_image_cut(img, div_v, div_h):
    h, w = img.shape[:2]
    block_h, out_h = divmod(h, div_v)
    block_w, out_w = divmod(w, div_h)
    block_shape = (block_h, block_w, 3) if len(img.shape) == 3 else (block_h, block_w)
    return skimage.util.view_as_blocks(img[:h - out_h, :w - out_w], block_shape)

blocks = split_image_cut(img, 2, 3)
print(blocks.shape)
# (2, 3, 1, 256, 170, 3)

print(blocks[0, 0, 0].shape)
# (256, 170, 3)

print(blocks[0, 1, 0].shape)
# (256, 170, 3)

print(blocks[0, 2, 0].shape)
# (256, 170, 3)

print(blocks[1, 0, 0].shape)
# (256, 170, 3)

print(blocks[1, 1, 0].shape)
# (256, 170, 3)

print(blocks[1, 2, 0].shape)
# (256, 170, 3)

def split_image_unequal(img, div_v, div_h):
    l_v = np.array_split(img, div_v)
    return [np.array_split(img_v, div_h, 1) for img_v in l_v]

l = split_image_unequal(img, 2, 3)

print(type(l))
# <class 'list'>

print(len(l))
# 2

print(type(l[0]))
# <class 'list'>

print(len(l[0]))
# 3

print(type(l[0][0]))
# <class 'numpy.ndarray'>

print(l[0][0].shape)
# (256, 171, 3)

print(l[0][1].shape)
# (256, 171, 3)

print(l[0][2].shape)
# (256, 170, 3)

print(l[1][0].shape)
# (256, 171, 3)

print(l[1][1].shape)
# (256, 171, 3)

print(l[1][2].shape)
# (256, 170, 3)

l_copy = split_image_unequal(img, 2, 3)

print(np.shares_memory(img, l[0][0]))
# True

l_copy = split_image_unequal(img.copy(), 2, 3)

print(np.shares_memory(img, l_copy[0][0]))
# False
