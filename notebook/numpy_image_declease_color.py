import numpy as np
from PIL import Image

im = np.array(Image.open('data/src/lena_square.png').resize((256, 256)))

im_32 = im // 32 * 32
im_128 = im // 128 * 128

im_dec = np.concatenate((im, im_32, im_128), axis=1)

Image.fromarray(im_dec).save('data/dst/lena_numpy_dec_color.png')
