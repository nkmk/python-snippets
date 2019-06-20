import numpy as np
from PIL import Image

img = np.array(Image.open('data/src/lena.jpg'))
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

Image.fromarray(np.rot90(img)).save('data/dst/lena_np_rot90.jpg')

Image.fromarray(np.rot90(img, 2)).save('data/dst/lena_np_rot90_180.jpg')

Image.fromarray(np.rot90(img, 3)).save('data/dst/lena_np_rot90_270.jpg')
