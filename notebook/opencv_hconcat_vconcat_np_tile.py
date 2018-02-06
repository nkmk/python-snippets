import cv2
import numpy as np

im1 = cv2.imread('data/src/lena.jpg')
im2 = cv2.imread('data/src/rocket.jpg')

im_v = cv2.vconcat([im1, im1])
cv2.imwrite('data/dst/opencv_vconcat.jpg', im_v)
# True

im_v_np = np.tile(im1, (2, 1, 1))
cv2.imwrite('data/dst/opencv_vconcat_np.jpg', im_v_np)
# True

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

im_v_resize = vconcat_resize_min([im1, im2, im1])
cv2.imwrite('data/dst/opencv_vconcat_resize.jpg', im_v_resize)
# True

im_h = cv2.hconcat([im1, im1])
cv2.imwrite('data/dst/opencv_hconcat.jpg', im_h)
# True

im_h_np = np.tile(im1, (1, 2, 1))
cv2.imwrite('data/dst/opencv_hconcat_np.jpg', im_h_np)
# True

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

im_h_resize = hconcat_resize_min([im1, im2, im1])
cv2.imwrite('data/dst/opencv_hconcat_resize.jpg', im_h_resize)
# True

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

im1_s = cv2.resize(im1, dsize=(0, 0), fx=0.5, fy=0.5)
im_tile = concat_tile([[im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s]])
cv2.imwrite('data/dst/opencv_concat_tile.jpg', im_tile)
# True

im_tile_np = np.tile(im1_s, (3, 4, 1))
cv2.imwrite('data/dst/opencv_concat_tile_np.jpg', im_tile_np)
# True

def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)

im_tile_resize = concat_tile_resize([[im1],
                                     [im1, im2, im1, im2, im1],
                                     [im1, im2, im1]])
cv2.imwrite('data/dst/opencv_concat_tile_resize.jpg', im_tile_resize)
# True
