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

im = cv2.imread('xxxxxxx')

print(im)
# None

# print(im.shape)
# AttributeError: 'NoneType' object has no attribute 'shape'

im = cv2.imread('data/src/sample.csv')

print(im)
# None

im = cv2.imread('xxxxxxx')

if im:
    print('Image is read.')
else:
    print('Image is not read.')
# Image is not read.

im = cv2.imread('xxxxxxx')

if not im:
    print('Image is not read.')
else:
    print('Image is read.')
# Image is not read.
