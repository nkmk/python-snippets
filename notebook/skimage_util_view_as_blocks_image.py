import numpy as np

import skimage.io
import skimage.util

img = skimage.io.imread('data/src/lena_square.png')
print(img.shape)
# (512, 512, 3)

blocks = skimage.util.view_as_blocks(img, (256, 256, 3))
print(blocks.shape)
# (2, 2, 1, 256, 256, 3)

# blocks = skimage.util.view_as_blocks(img, (256, 256))
# ValueError: 'block_shape' must have the same length as 'arr_in.shape'

print(blocks[0, 0, 0].shape)
# (256, 256, 3)

skimage.io.imsave('data/dst/skimage_block_00.jpg', blocks[0, 0, 0])
skimage.io.imsave('data/dst/skimage_block_01.jpg', blocks[0, 1, 0])
skimage.io.imsave('data/dst/skimage_block_10.jpg', blocks[1, 0, 0])
skimage.io.imsave('data/dst/skimage_block_11.jpg', blocks[1, 1, 0])

print(np.shares_memory(img, blocks))
# True

blocks[0, 0, 0] = 0
blocks[1, 1, 0] //= 2

skimage.io.imsave('data/dst/skimage_block_change.jpg', img)

blocks_s = skimage.util.view_as_blocks(img, (256, 256, 3)).squeeze()
print(blocks_s.shape)
# (2, 2, 256, 256, 3)

print(blocks_s[0, 0].shape)
# (256, 256, 3)
