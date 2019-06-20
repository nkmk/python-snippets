import numpy as np
from PIL import Image

img = np.array(Image.open('data/src/lena.jpg'))
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

Image.fromarray(np.flipud(img)).save('data/dst/lena_np_flipud.jpg')

Image.fromarray(np.fliplr(img)).save('data/dst/lena_np_fliplr.jpg')

Image.fromarray(np.flip(img, (0, 1))).save('data/dst/lena_np_flip_ud_lr.jpg')
