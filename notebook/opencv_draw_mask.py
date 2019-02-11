import cv2
import numpy as np

src = cv2.imread('data/src/lena.jpg')

mask = np.zeros_like(src)

print(mask.shape)
# (225, 400, 3)

print(mask.dtype)
# uint8

cv2.rectangle(mask, (50, 50), (100, 200), (255, 255, 255), thickness=-1)
cv2.circle(mask, (200, 100), 50, (255, 255, 255), thickness=-1)
cv2.fillConvexPoly(mask, np.array([[330, 50], [300, 200], [360, 150]]), (255, 255, 255))

cv2.imwrite('data/dst/opencv_draw_mask.jpg', mask)
# True

# ![](data/dst/opencv_draw_mask.jpg)

mask_blur = cv2.GaussianBlur(mask, (51, 51), 0)

cv2.imwrite('data/dst/opencv_draw_mask_blur.jpg', mask_blur)
# True

# ![](data/dst/opencv_draw_mask_blur.jpg)

dst = src * (mask_blur / 255)

cv2.imwrite('data/dst/opencv_draw_mask_blur_result.jpg', dst)
# True

# ![](data/dst/opencv_draw_mask_blur_result.jpg)
