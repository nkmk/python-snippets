import cv2

im = cv2.imread('data/src/lena.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)  # サイズ（高さ x 幅 x 色数）
# (225, 400, 3)

print(im.dtype)
# uint8

im[:, :, (0, 1)] = 0

cv2.imwrite('data/dst/lena_opencv_red.jpg', im)
# True

im_gray = cv2.imread('data/src/lena.jpg', cv2.IMREAD_GRAYSCALE)
# im_gray = cv2.imread('data/src/lena.jpg', 0)

print(type(im_gray))
# <class 'numpy.ndarray'>

print(im_gray.shape)  # サイズ（高さ x 幅）
# (225, 400)

print(im_gray.dtype)
# uint8

cv2.imwrite('data/dst/lena_opencv_gray.jpg', im_gray)
# True
