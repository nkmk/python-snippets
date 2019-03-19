import numpy as np
from PIL import Image

img = np.array(Image.open('data/src/lena.jpg'))

print(img.shape)
# (225, 400, 3)

img_scroll = np.roll(img, (50, 100), axis=(0, 1))

Image.fromarray(img_scroll).save('data/dst/lena_numpy_roll.jpg')
