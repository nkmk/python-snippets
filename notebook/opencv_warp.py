import cv2
import numpy as np

src = cv2.imread('data/src/lena.jpg')
dst = cv2.imread('data/src/rocket.jpg')

src_pts = [[100, 80], [150, 200], [300, 20]]
dst_pts = [[280, 120], [320, 300], [400, 150]]

src_mark = src.copy()

for pt in src_pts:
    cv2.drawMarker(src_mark, tuple(pt), (0, 255, 0), thickness=4)

cv2.imwrite('data/dst/opencv_warp_src_mark.jpg', src_mark)
# True

# ![](data/dst/opencv_warp_mark.jpg)

dst_mark = dst.copy()

for pt in dst_pts:
    cv2.drawMarker(dst_mark, tuple(pt), (0, 255, 0), thickness=4)

cv2.imwrite('data/dst/opencv_warp_dst_mark.jpg', dst_mark)
# True

# ![](data/dst/opencv_warp_dst_mark.jpg)

src_pts_arr = np.array(src_pts, dtype=np.float32)
dst_pts_arr = np.array(dst_pts, dtype=np.float32)

src_rect = cv2.boundingRect(src_pts_arr)
dst_rect = cv2.boundingRect(dst_pts_arr)

print(src_rect)
# (100, 20, 201, 181)

print(dst_rect)
# (280, 120, 121, 181)

src_crop = src[src_rect[1]:src_rect[1] + src_rect[3], src_rect[0]:src_rect[0] + src_rect[2]]
dst_crop = dst[dst_rect[1]:dst_rect[1] + dst_rect[3], dst_rect[0]:dst_rect[0] + dst_rect[2]]

src_pts_crop = src_pts_arr - src_rect[:2]
dst_pts_crop = dst_pts_arr - dst_rect[:2]

print(src_pts_crop)
# [[  0.  60.]
#  [ 50. 180.]
#  [200.   0.]]

print(dst_pts_crop)
# [[  0.   0.]
#  [ 40. 180.]
#  [120.  30.]]

src_crop_mark = src_crop.copy()

for pt in src_pts_crop.astype(np.int):
    cv2.drawMarker(src_crop_mark, tuple(pt), (0, 255, 0), thickness=4)

cv2.imwrite('data/dst/opencv_warp_src_crop_mark.jpg', src_crop_mark)
# True

# ![](data/dst/opencv_warp_src_crop_mark.jpg)

dst_crop_mark = dst_crop.copy()

for pt in dst_pts_crop.astype(np.int):
    cv2.drawMarker(dst_crop_mark, tuple(pt), (0, 255, 0), thickness=4)

cv2.imwrite('data/dst/opencv_warp_dst_crop_mark.jpg', dst_crop_mark)
# True

# ![](data/dst/opencv_warp_dst_crop_mark.jpg)

mat = cv2.getAffineTransform(src_pts_crop.astype(np.float32), dst_pts_crop.astype(np.float32))
affine_img = cv2.warpAffine(src_crop, mat, tuple(dst_rect[2:]))

cv2.imwrite('data/dst/opencv_warp_affine_crop.jpg', affine_img)
# True

# ![](data/dst/opencv_warp_affine_crop.jpg)

mask = np.zeros_like(dst_crop, dtype=np.float32)
cv2.fillConvexPoly(mask, dst_pts_crop.astype(np.int), (1.0, 1.0, 1.0), cv2.LINE_AA)

dst_crop_merge = affine_img * mask + dst_crop * (1 - mask)

cv2.imwrite('data/dst/opencv_warp_affine_crop_merge.jpg', dst_crop_merge)
# True

# ![](data/dst/opencv_warp_affine_crop_merge.jpg)

dst[dst_rect[1]:dst_rect[1] + dst_rect[3], dst_rect[0]:dst_rect[0] + dst_rect[2]] = dst_crop_merge

cv2.imwrite('data/dst/opencv_warp_dst_result.jpg', dst)
# True

# ![](data/dst/opencv_warp_dst.jpg)
