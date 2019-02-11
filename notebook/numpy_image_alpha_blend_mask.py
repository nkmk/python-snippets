import numpy as np
from PIL import Image

src1 = np.array(Image.open('data/src/lena.jpg'))
src2 = np.array(Image.open('data/src/rocket.jpg').resize(src1.shape[1::-1], Image.BILINEAR))

mask1 = np.array(Image.open('data/src/gradation_h.jpg').resize(src1.shape[1::-1], Image.BILINEAR))

mask1 = mask1 / 255

dst = src1 * mask1 + src2 * (1 - mask1)

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_ab_grad.jpg')

# ![](data/dst/numpy_image_ab_grad.jpg)

mask2 = np.array(Image.open('data/src/horse_r.png').resize(src1.shape[1::-1], Image.BILINEAR))

mask2 = mask2 / 255

dst = (src1 * mask1 + src2 * (1 - mask1)) * mask2

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_ab_mask_grad.jpg')

# ![](data/dst/numpy_image_ab_mask_grad.jpg)
