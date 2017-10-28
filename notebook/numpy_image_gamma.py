from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'), 'f')  # floatで読み込み

im_1_22 = 255.0 * (im / 255.0)**(1 / 2.2)
im_22 = 255.0 * (im / 255.0)**2.2

im_gamma = np.concatenate((im_1_22, im, im_22), axis=1)

pil_img = Image.fromarray(np.uint8(im_gamma))  # floatをuintに変換
pil_img.save('data/dst/lena_gamma.jpg')
