import cv2
import numpy as np

def warp(src, dst, src_pts, dst_pts, transform_func, warp_func, **kwargs):
    src_pts_arr = np.array(src_pts, dtype=np.float32)
    dst_pts_arr = np.array(dst_pts, dtype=np.float32)
    src_rect = cv2.boundingRect(src_pts_arr)
    dst_rect = cv2.boundingRect(dst_pts_arr)
    src_crop = src[src_rect[1]:src_rect[1] + src_rect[3], src_rect[0]:src_rect[0] + src_rect[2]]
    dst_crop = dst[dst_rect[1]:dst_rect[1] + dst_rect[3], dst_rect[0]:dst_rect[0] + dst_rect[2]]
    src_pts_crop = src_pts_arr - src_rect[:2]
    dst_pts_crop = dst_pts_arr - dst_rect[:2]
    
    mat = transform_func(src_pts_crop.astype(np.float32), dst_pts_crop.astype(np.float32))
    warp_img = warp_func(src_crop, mat, tuple(dst_rect[2:]), **kwargs)
    
    mask = np.zeros_like(dst_crop, dtype=np.float32)
    cv2.fillConvexPoly(mask, dst_pts_crop.astype(np.int), (1.0, 1.0, 1.0), cv2.LINE_AA)
    
    dst_crop_merge = warp_img * mask + dst_crop * (1 - mask)
    dst[dst_rect[1]:dst_rect[1] + dst_rect[3], dst_rect[0]:dst_rect[0] + dst_rect[2]] = dst_crop_merge

def warp_triangle(src, dst, src_pts, dst_pts, **kwargs):
    warp(src, dst, src_pts, dst_pts,
         cv2.getAffineTransform, cv2.warpAffine, **kwargs)

def warp_rectangle(src, dst, src_pts, dst_pts, **kwargs):
    warp(src, dst, src_pts, dst_pts,
         cv2.getPerspectiveTransform, cv2.warpPerspective, **kwargs)

src = cv2.imread('data/src/lena.jpg')
dst = cv2.imread('data/src/rocket.jpg')

src_pts = [[100, 80], [150, 200], [300, 20]]
dst_pts = [[280, 120], [320, 300], [400, 150]]

warp_triangle(src, dst, src_pts, dst_pts)

cv2.imwrite('data/dst/opencv_warp_triangle.jpg', dst)
# True

# ![](data/dst/opencv_warp_triangle.jpg)

src = cv2.imread('data/src/lena.jpg')
dst = cv2.imread('data/src/rocket.jpg')

src_pts = [[100, 80], [150, 200], [350, 160], [300, 20]]
dst_pts = [[280, 120], [200, 280], [500, 300], [400, 150]]

warp_rectangle(src, dst, src_pts, dst_pts, flags=cv2.INTER_CUBIC)

cv2.imwrite('data/dst/opencv_warp_rectangle.jpg', dst)
# True

# ![](data/dst/opencv_warp_rectangle.jpg)
