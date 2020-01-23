import cv2
import numpy as np

im = cv2.imread('data/src/lena.jpg')
print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(im_gray.shape)
# (225, 400)

print(im_gray.dtype)
# uint8

cv2.imwrite('data/dst/opencv_gray_cvtcolr.jpg', im_gray)
# True

im_gray_read = cv2.imread('data/src/lena.jpg', cv2.IMREAD_GRAYSCALE)
print(im_gray_read.shape)
# (225, 400)

print(im_gray_read.dtype)
# uint8

cv2.imwrite('data/dst/opencv_gray_imread.jpg', im_gray_read)
# True

im_gray_diff = im_gray.astype(int) - im_gray_read.astype(int)

print(im_gray_diff.max())
# 10

print(im_gray_diff.min())
# -10

im_gray_calc = 0.299 * im[:, :, 2] + 0.587 * im[:, :, 1] + 0.114 * im[:, :, 0]
print(im_gray_calc.shape)
# (225, 400)

print(im_gray_calc.dtype)
# float64

cv2.imwrite('data/dst/numpy_gray_calc.jpg', im_gray_calc)
# True

im_gray_diff = im_gray_calc - im_gray

print(im_gray_diff.max())
# 0.4969999999999857

print(im_gray_diff.min())
# -0.4980000000000473

a = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

print(a.round())
# [0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1.]

print(a.astype('uint8'))
# [0 0 0 0 0 0 0 0 0 0 1]

print(np.array_equal(im_gray_calc.round(), im_gray))
# True

print(np.array_equal(im_gray_calc.astype('uint8'), im_gray))
# False
