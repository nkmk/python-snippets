import numpy as np
from PIL import Image

im = np.array(Image.open('data/src/lena_square.png').resize((256, 256)))

im_i = 255 - im

Image.fromarray(im_i).save('data/dst/lena_numpy_inverse.jpg')
