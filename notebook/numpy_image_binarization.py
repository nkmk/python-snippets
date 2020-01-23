import numpy as np
from PIL import Image

im_gray = np.array(Image.open('data/src/lena_square_half.png').convert('L'))
print(type(im_gray))
# <class 'numpy.ndarray'>

thresh = 128

im_bool = im_gray > thresh
print(im_bool)
# [[ True  True  True ...  True  True False]
#  [ True  True  True ...  True  True False]
#  [ True  True  True ...  True False False]
#  ...
#  [False False False ... False False False]
#  [False False False ... False False False]
#  [False False False ... False False False]]

maxval = 255

im_bin = (im_gray > thresh) * maxval
print(im_bin)
# [[255 255 255 ... 255 255   0]
#  [255 255 255 ... 255 255   0]
#  [255 255 255 ... 255   0   0]
#  ...
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]]

Image.fromarray(np.uint8(im_bin)).save('data/dst/numpy_binarization.png')

im_bin_keep = (im_gray > thresh) * im_gray
print(im_bin_keep)
# [[162 161 156 ... 169 169   0]
#  [162 161 156 ... 169 169   0]
#  [164 155 159 ... 145   0   0]
#  ...
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]
#  [  0   0   0 ...   0   0   0]]

Image.fromarray(np.uint8(im_bin_keep)).save('data/dst/numpy_binarization_keep.png')

im_bool = im_gray > 128
im_dst = np.empty((*im_gray.shape, 3))
r, g, b = 255, 128, 32

im_dst[:, :, 0] = im_bool * r
im_dst[:, :, 1] = im_bool * g
im_dst[:, :, 2] = im_bool * b

Image.fromarray(np.uint8(im_dst)).save('data/dst/numpy_binarization_color.png')

im_bool = im_gray > 128
im_dst = np.empty((*im_gray.shape, 3))
r, g, b = 128, 160, 192

im_dst[:, :, 0] = im_bool * r
im_dst[:, :, 1] = ~im_bool * g
im_dst[:, :, 2] = im_bool * b

Image.fromarray(np.uint8(im_dst)).save('data/dst/numpy_binarization_color2.png')

im = np.array(Image.open('data/src/lena_square_half.png'))

im_th = np.empty_like(im)

thresh = 128
maxval = 255

for i in range(3):
    im_th[:, :, i] = (im[:, :, i] > thresh) * maxval

Image.fromarray(np.uint8(im_th)).save('data/dst/numpy_binarization_from_color.png')

l_thresh = [64, 128, 192]
l_maxval = [64, 128, 192]

for i, thresh, maxval in zip(range(3), l_thresh, l_maxval):
    im_th[:, :, i] = (im[:, :, i] > thresh) * maxval

Image.fromarray(np.uint8(im_th)).save('data/dst/numpy_binarization_from_color2.png')
