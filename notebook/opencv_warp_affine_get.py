import cv2
import numpy as np

img = cv2.imread('data/src/lena.jpg')

h, w, c = img.shape

# ![](data/src/lena.jpg)

src_pts = np.array([[30, 30], [50, 200], [350, 50]], dtype=np.float32)
dst_pts = np.array([[90, 20], [140, 170], [280, 80]], dtype=np.float32)

mat = cv2.getAffineTransform(src_pts, dst_pts)
print(mat)
# [[  0.57962963   0.22592593  65.83333333]
#  [  0.13333333   0.86666667 -10.        ]]

img_mark = img.copy()

for pt in src_pts:
    cv2.drawMarker(img_mark, tuple(pt), (0, 255, 0), thickness=4)

cv2.imwrite('data/dst/opencv_affine_mark_src.jpg', img_mark)
# True

# ![](data/dst/opencv_affine_mark.jpg)

affine_img = cv2.warpAffine(img_mark, mat, (w, h))
cv2.imwrite('data/dst/opencv_affine_mark_dst.jpg', affine_img)
# True

# ![](data/dst/opencv_affine_mark_dst.jpg)

affine_img_mark = affine_img.copy()

for pt in dst_pts:
    cv2.drawMarker(affine_img_mark, tuple(pt), (255, 0, 0), markerType=cv2.MARKER_SQUARE, thickness=4)

cv2.imwrite('data/dst/opencv_affine_mark_dst_mark.jpg', affine_img_mark)
# True

# ![](data/dst/opencv_affine_mark_dst_mark.jpg)

src_pts = np.array([[30, 30], [50, 200], [350, 50]], dtype=np.float32)
dst_pts = np.array([[140, 170], [280, 80], [90, 20]], dtype=np.float32)

mat = cv2.getAffineTransform(src_pts, dst_pts)
print(mat)
# [[ -0.20925926   0.84814815 120.83333333]
#  [ -0.43888889  -0.47777778 197.5       ]]

affine_img = cv2.warpAffine(img_mark, mat, (w, h))
cv2.imwrite('data/dst/opencv_affine_mark_dst_another.jpg', affine_img)
# True

# ![](data/dst/opencv_affine_mark_dst_another.jpg)
