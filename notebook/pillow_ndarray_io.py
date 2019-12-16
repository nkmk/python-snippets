from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena.jpg'))

print(type(im))
# <class 'numpy.ndarray'>

print(im.dtype)
# uint8

print(im.shape)
# (225, 400, 3)

im_gray = np.array(Image.open('data/src/lena.jpg').convert('L'))

print(im_gray.shape)
# (225, 400)

print(im.flags.writeable)
# True

print(im[0, 0, 0])
# 109

im[0, 0, 0] = 0

print(im[0, 0, 0])
# 0

im_as = np.asarray(Image.open('data/src/lena.jpg'))

print(type(im_as))
# <class 'numpy.ndarray'>

print(im_as.flags.writeable)
# False

# im_as[0, 0, 0] = 0
# ValueError: assignment destination is read-only

im_f = im.astype(np.float64)
print(im_f.dtype)
# float64

im_f = np.array(Image.open('data/src/lena.jpg'), np.float64)
print(im_f.dtype)
# float64

print(im_gray.dtype)
# uint8

pil_img = Image.fromarray(im)
print(pil_img.mode)
# RGB

pil_img.save('data/temp/lena_save_pillow.jpg')

pil_img_gray = Image.fromarray(im_gray)
print(pil_img_gray.mode)
# L

pil_img_gray.save('data/temp/lena_save_pillow_gray.jpg')

Image.fromarray(im).save('data/temp/lena_save_pillow.jpg')
Image.fromarray(im_gray).save('data/temp/lena_save_pillow_gray.jpg')

# pil_img = Image.fromarray(im_f)
# TypeError: Cannot handle this data type

pil_img = Image.fromarray(im_f.astype(np.uint8))
pil_img.save('data/temp/lena_save_pillow.jpg')
