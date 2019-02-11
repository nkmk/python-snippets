import numpy as np
from PIL import Image

src1 = np.array(Image.open('data/src/lena.jpg'))
src2 = np.array(Image.open('data/src/rocket.jpg').resize(src1.shape[1::-1], Image.BILINEAR))

print(src1.dtype)
# uint8

dst = src1 * 0.5 + src2 * 0.5

print(dst.dtype)
# float64

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_alpha_blend.jpg')

# ![](data/dst/numpy_image_alpha_blend.jpg)

dst = src1 * 0.5 + src2 * 0.2 + (96, 128, 160)

print(dst.max())
# 311.1

dst = dst.clip(0, 255)

print(dst.max())
# 255.0

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_alpha_blend_gamma.jpg')

# ![](data/dst/numpy_image_alpha_blend_gamma.jpg)
