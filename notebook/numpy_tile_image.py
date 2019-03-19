import numpy as np
from PIL import Image

img = np.array(Image.open('data/src/lena_square.png').resize((128, 128)))

print(img.shape)
# (128, 128, 3)

img_tile = np.tile(img, (2, 3, 1))

print(img_tile.shape)
# (256, 384, 3)

Image.fromarray(img_tile).save('data/dst/lena_numpy_tile.jpg')
