from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png').resize((256, 256)))

print(im.shape)
# (256, 256, 3)

im_0 = im[:, :100]
im_1 = im[:, 100:]

print(im_0.shape)
# (256, 100, 3)

print(im_1.shape)
# (256, 156, 3)

Image.fromarray(im_0).save('data/dst/lena_numpy_split_0.jpg')
Image.fromarray(im_1).save('data/dst/lena_numpy_split_1.jpg')

im_0, im_1 = np.hsplit(im, 2)

print(im_0.shape)
# (256, 128, 3)

print(im_1.shape)
# (256, 128, 3)

im_0, im_1, im_2 = np.hsplit(im, [100, 150])

print(im_0.shape)
# (256, 100, 3)

print(im_1.shape)
# (256, 50, 3)

print(im_2.shape)
# (256, 106, 3)

# im_0, im_1, im_2 = np.hsplit(im, 3)
# ValueError: array split does not result in an equal division

im_0, im_1, im_2 = np.array_split(im, 3, axis=1)

print(im_0.shape)
# (256, 86, 3)

print(im_1.shape)
# (256, 85, 3)

print(im_2.shape)
# (256, 85, 3)
