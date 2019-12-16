from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena.jpg'))

print(im.shape)
# (225, 400, 3)

print(im[100, 150])
# [111  81 109]

print(type(im[100, 150]))
# <class 'numpy.ndarray'>

R, G, B = im[100, 150]

print(R)
# 111

print(G)
# 81

print(B)
# 109

print(im[100, 150, 0])
# 111

print(im[100, 150, 1])
# 81

print(im[100, 150, 2])
# 109

im[100, 150] = (0, 50, 100)

print(im[100, 150])
# [  0  50 100]

im[100, 150, 0] = 150

print(im[100, 150])
# [150  50 100]
