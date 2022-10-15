import cv2

im = cv2.imread('data/src/lena.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8

im[:, :, (0, 1)] = 0

cv2.imwrite('data/dst/lena_opencv_red.jpg', im)
# True

cv2.imwrite('data/dst/lena_opencv_red_high.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 100])
# True

cv2.imwrite('data/dst/lena_opencv_red_low.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 50])
# True

im_gray = cv2.imread('data/src/lena.jpg', cv2.IMREAD_GRAYSCALE)
# im_gray = cv2.imread('data/src/lena.jpg', 0)

print(type(im_gray))
# <class 'numpy.ndarray'>

print(im_gray.shape)
# (225, 400)

print(im_gray.dtype)
# uint8

cv2.imwrite('data/dst/lena_opencv_gray.jpg', im_gray)
# True

im_gray_read = cv2.imread('data/dst/lena_opencv_gray.jpg')

print(im_gray_read.shape)
# (225, 400, 3)

import numpy as np

print(np.array_equal(im_gray_read[:, :, 0], im_gray_read[:, :, 1]))
# True

print(np.array_equal(im_gray_read[:, :, 1], im_gray_read[:, :, 2]))
# True

im_not_exist = cv2.imread('xxxxxxx')
# [ WARN:0@0.069] global /tmp/opencv-20221012-82716-1q8maeo/opencv-4.6.0/modules/imgcodecs/src/loadsave.cpp (239) findDecoder imread_('xxxxxxx'): can't open/read file: check file path/integrity

print(im_not_exist)
# None

# print(im_not_exist.shape)
# AttributeError: 'NoneType' object has no attribute 'shape'

im_not_supported = cv2.imread('data/src/sample.csv')

print(im_not_supported)
# None

if im_not_exist is not None:
    print('Image is read.')
else:
    print('Image is not read.')
# Image is not read.

if im_not_exist is None:
    print('Image is not read.')
else:
    print('Image is read.')
# Image is not read.

im = cv2.imread('data/src/lena.jpg')

if im is not None:
    print('Image is read.')
else:
    print('Image is not read.')
# Image is read.

if im is None:
    print('Image is not read.')
else:
    print('Image is read.')
# Image is read.
