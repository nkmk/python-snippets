import cv2
import numpy as np
from PIL import Image

im_cv = cv2.imread('data/src/lena.jpg')

cv2.imwrite('data/dst/lena_bgr_cv.jpg', im_cv)
# True

pil_img = Image.fromarray(im_cv)
pil_img.save('data/dst/lena_bgr_pillow.jpg')

im_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)

Image.fromarray(im_rgb).save('data/dst/lena_rgb_pillow.jpg')

cv2.imwrite('data/dst/lena_rgb_cv.jpg', im_rgb)
# True

im_pillow = np.array(Image.open('data/src/lena.jpg'))

im_bgr = cv2.cvtColor(im_pillow, cv2.COLOR_RGB2BGR)

cv2.imwrite('data/dst/lena_bgr_cv_2.jpg', im_bgr)
# True

im_bgr = cv2.imread('data/src/lena.jpg')

im_rgb = im_bgr[:, :, [2, 1, 0]]
Image.fromarray(im_rgb).save('data/dst/lena_swap.jpg')

im_rgb = im_bgr[:, :, ::-1]
Image.fromarray(im_rgb).save('data/dst/lena_swap_2.jpg')
