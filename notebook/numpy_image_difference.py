import cv2
import numpy as np

im = cv2.imread('data/src/lena.jpg')
print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8

cv2.imwrite('data/temp/lena.png', im)
im_png = cv2.imread('data/temp/lena.png')

print(np.array_equal(im, im_png))
# True

cv2.imwrite('data/temp/lena.bmp', im)
im_bmp = cv2.imread('data/temp/lena.bmp')

print(np.array_equal(im, im_bmp))
# True

print(np.array_equal(im_png, im_bmp))
# True

cv2.imwrite('data/dst/lena_q25.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 25])
im_q25 = cv2.imread('data/dst/lena_q25.jpg')

print(np.array_equal(im, im_q25))
# False

print(im.shape == im_q25.shape)
# True

print(im.shape == (250, 400, 3))
# False

im_diff = im.astype(int) - im_q25.astype(int)

print(im_diff.max())
# 142

print(im_diff.min())
# -101

im_diff_abs = np.abs(im_diff)

print(im_diff_abs.max())
# 142

print(im_diff_abs.min())
# 0

cv2.imwrite('data/dst/lena_diff_abs.png', im_diff_abs)
# True

im_diff_abs_norm = im_diff_abs / im_diff_abs.max() * 255

print(im_diff_abs_norm.max())
# 255.0

print(im_diff_abs_norm.min())
# 0.0

cv2.imwrite('data/dst/lena_diff_abs_norm.png', im_diff_abs_norm)
# True

im_diff_center = np.floor_divide(im_diff, 2) + 128

print(im_diff_center.max())
# 199

print(im_diff_center.min())
# 77

cv2.imwrite('data/dst/lena_diff_center.png', im_diff_center)
# True

im_diff_center_norm = im_diff / np.abs(im_diff).max() * 127.5 + 127.5

print(im_diff_center_norm.max())
# 255.0

print(im_diff_center_norm.min())
# 36.81338028169013

cv2.imwrite('data/dst/lena_diff_center_norm.png', im_diff_center_norm)
# True

im_diff_bin = (im_diff_abs > 32) * 255

cv2.imwrite('data/dst/lena_diff_bin.png', im_diff_bin)
# True

print(list(zip(*np.where(im_diff_abs == np.max(im_diff_abs)))))
# [(155, 117, 2)]

print(list(zip(*np.where(im_diff_abs > 100))))
# [(135, 160, 0), (137, 157, 2), (155, 117, 2)]
