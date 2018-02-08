import numpy as np
from PIL import Image

im = np.array(Image.open('data/src/lena_square.png').convert('L').resize((256, 256)))
print(type(im))
# <class 'numpy.ndarray'>

th = 128
im_bool = im > th
print(im_bool)
# [[ True  True  True ...,  True  True False]
#  [ True  True  True ...,  True  True False]
#  [ True  True  True ...,  True False False]
#  ..., 
#  [False False False ..., False False False]
#  [False False False ..., False False False]
#  [False False False ..., False False False]]

im_bin_128 = (im > th) * 255
print(im_bin_128)
# [[255 255 255 ..., 255 255   0]
#  [255 255 255 ..., 255 255   0]
#  [255 255 255 ..., 255   0   0]
#  ..., 
#  [  0   0   0 ...,   0   0   0]
#  [  0   0   0 ...,   0   0   0]
#  [  0   0   0 ...,   0   0   0]]

im_bin_64 = (im > 64) * 255
im_bin_192 = (im > 192) * 255

im_bin = np.concatenate((im_bin_64, im_bin_128, im_bin_192), axis=1)
Image.fromarray(np.uint8(im_bin)).save('data/dst/lena_numpy_binarization.png')

im_bool = im > 128
h, w = im.shape

im_dst = np.empty((h, w, 3))

r, g, b = 255, 128, 32

im_dst[:, :, 0] = im_bool * r
im_dst[:, :, 1] = im_bool * g
im_dst[:, :, 2] = im_bool * b

Image.fromarray(np.uint8(im_dst)).save('data/dst/lena_numpy_binarization_color.png')

r, g, b = 128, 160, 192

im_dst[:, :, 0] = im_bool * r
im_dst[:, :, 1] = ~im_bool * g
im_dst[:, :, 2] = im_bool * b

Image.fromarray(np.uint8(im_dst)).save('data/dst/lena_numpy_binarization_color2.png')
