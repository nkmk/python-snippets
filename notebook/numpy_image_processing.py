from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

print(im.dtype)
# uint8

print(im.ndim)
# 3

print(im.shape)
# (512, 512, 3)

im_f = np.array(Image.open('data/src/lena_square.png'), np.float)

print(im_f.dtype)
# float64

print(im[256, 256])
# [180  65  72]

print(im[:, :, 0].min())
# 54

pil_img = Image.fromarray(im)
pil_img.save('data/temp/lena_square_save.png')

Image.fromarray(im).save('data/temp/lena_square_save.png')

pil_img_f = Image.fromarray(im_f.astype(np.uint8))
pil_img_f.save('data/temp/lena_square_save.png')
