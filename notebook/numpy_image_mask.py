import numpy as np
from PIL import Image

src = np.array(Image.open('data/src/lena.jpg'))
mask = np.array(Image.open('data/src/horse_r.png').resize(src.shape[1::-1], Image.BILINEAR))

print(mask.dtype, mask.min(), mask.max())
# uint8 0 255

mask = mask / 255

print(mask.dtype, mask.min(), mask.max())
# float64 0.0 1.0

dst = src * mask

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_mask.jpg')

# ![](data/dst/numpy_image_mask.jpg)

mask = np.array(Image.open('data/src/horse_r.png').convert('L').resize(src.shape[1::-1], Image.BILINEAR))

print(mask.shape)
# (225, 400)

mask = mask / 255

# dst = src * mask
# ValueError: operands could not be broadcast together with shapes (225,400,3) (225,400) 

# mask = mask[:, :, np.newaxis]

mask = mask.reshape(*mask.shape, 1)

print(mask.shape)
# (225, 400, 1)

dst = src * mask

Image.fromarray(dst.astype(np.uint8)).save('data/dst/numpy_image_mask_l.jpg')

# ![](data/dst/numpy_image_mask_l.jpg)
