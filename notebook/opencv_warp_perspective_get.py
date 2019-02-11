import cv2
import numpy as np

img = cv2.imread('data/src/lena.jpg')

h, w, c = img.shape

# ![](data/src/lena.jpg)

src_pts = np.array([[0, 0], [0, h], [w, h], [w, 0]], dtype=np.float32)
dst_pts = np.array([[20, 50], [50, 175], [300, 205], [380, 20]], dtype=np.float32)

mat = cv2.getPerspectiveTransform(src_pts, dst_pts)
print(mat)
# [[ 5.42651593e-01  2.04362225e-01  2.00000000e+01]
#  [-9.38078109e-02  8.04156675e-01  5.00000000e+01]
#  [-9.40390545e-04  1.42057782e-03  1.00000000e+00]]

perspective_img = cv2.warpPerspective(img, mat, (w, h))
cv2.imwrite('data/dst/opencv_perspective_dst.jpg', perspective_img)
# True

# ![](data/dst/opencv_perspective_dst.jpg)

mat_i = cv2.getPerspectiveTransform(dst_pts, src_pts)
print(mat_i)
# [[ 1.60933274e+00 -3.86239857e-01 -1.28746619e+01]
#  [ 1.02707766e-01  1.23249319e+00 -6.36788147e+01]
#  [ 1.36749691e-03 -2.11406880e-03  1.00000000e+00]]

perspective_img_i = cv2.warpPerspective(perspective_img, mat_i, (w, h))
cv2.imwrite('data/dst/opencv_perspective_dst_inverse.jpg', perspective_img_i)
# True

# ![](data/dst/opencv_perspective_dst_inverse.jpg)
