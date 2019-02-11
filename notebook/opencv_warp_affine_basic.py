import cv2
import numpy as np

img = cv2.imread('data/src/lena.jpg')

h, w, c = img.shape
print(h, w, c)
# 225 400 3

# ![](data/src/lena.jpg)

mat = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 0.5)
print(mat)
# [[  0.35355339   0.35355339  89.51456544]
#  [ -0.35355339   0.35355339 143.43592168]]

affine_img = cv2.warpAffine(img, mat, (w, h))
cv2.imwrite('data/dst/opencv_affine.jpg', affine_img)
# True

# ![](data/dst/opencv_affine.jpg)

affine_img_half = cv2.warpAffine(img, mat, (w, h // 2))
cv2.imwrite('data/dst/opencv_affine_half.jpg', affine_img_half)
# True

# ![](data/dst/opencv_affine_half.jpg)

affine_img_flags = cv2.warpAffine(img, mat, (w, h), flags=cv2.INTER_CUBIC)
cv2.imwrite('data/dst/opencv_affine_flags.jpg', affine_img_flags)
# True

# ![](data/dst/opencv_affine_flags.jpg)

affine_img_bv = cv2.warpAffine(img, mat, (w, h), borderValue=(0, 128, 255))
cv2.imwrite('data/dst/opencv_affine_border_value.jpg', affine_img_bv)
# True

# ![](data/dst/opencv_affine_border_value.jpg)

dst = img // 4

affine_img_bm_bt = cv2.warpAffine(img, mat, (w, h), borderMode=cv2.BORDER_TRANSPARENT, dst=dst)
cv2.imwrite('data/dst/opencv_affine_border_transparent.jpg', affine_img_bm_bt)
# True

# ![](data/dst/opencv_affine_border_transparent.jpg)

affine_img_bm_br = cv2.warpAffine(img, mat, (w, h), borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('data/dst/opencv_affine_border_replicate.jpg', affine_img_bm_br)
# True

# ![](data/dst/opencv_affine_border_replicate.jpg)

affine_img_bm_bw = cv2.warpAffine(img, mat, (w, h), borderMode=cv2.BORDER_WRAP)
cv2.imwrite('data/dst/opencv_affine_border_wrap.jpg', affine_img_bm_bw)
# True

# ![](data/dst/opencv_affine_border_wrap.jpg)

mat = np.array([[1, 0, 50], [0, 1, 20]], dtype=np.float32)
print(mat)
# [[ 1.  0. 50.]
#  [ 0.  1. 20.]]

affine_img_translation = cv2.warpAffine(img, mat, (w, h))
cv2.imwrite('data/dst/opencv_affine_translation.jpg', affine_img_translation)
# True

# ![](data/dst/opencv_affine_translation.jpg)
