from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

print(im.shape)
# (512, 512, 3)

im_trim1 = im[128:384, 128:384]
print(im_trim1.shape)
# (256, 256, 3)

Image.fromarray(im_trim1).save('data/dst/lena_numpy_trim.jpg')

def trim(array, x, y, width, height):
    return array[y:y + height, x:x+width]

im_trim2 = trim(im, 128, 192, 256, 128)
print(im_trim2.shape)
# (128, 256, 3)

Image.fromarray(im_trim2).save('data/dst/lena_numpy_trim2.jpg')

im_trim3 = trim(im, 128, 192, 512, 128)
print(im_trim3.shape)
# (128, 384, 3)

Image.fromarray(im_trim3).save('data/dst/lena_numpy_trim3.jpg')
