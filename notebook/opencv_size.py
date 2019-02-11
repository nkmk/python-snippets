import cv2

im = cv2.imread('data/src/lena.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))
# (225, 400, 3)
# <class 'tuple'>

h, w, c = im.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
# width:   400
# height:  225
# channel: 3

h, w, _ = im.shape
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

print('width: ', im.shape[1])
print('height:', im.shape[0])
# width:  400
# height: 225

print(im.shape[1::-1])
# (400, 225)

im_gray = cv2.imread('data/src/lena.jpg', cv2.IMREAD_GRAYSCALE)

print(im_gray.shape)
print(type(im_gray.shape))
# (225, 400)
# <class 'tuple'>

h, w = im_gray.shape
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

print('width: ', im_gray.shape[1])
print('height:', im_gray.shape[0])
# width:  400
# height: 225

h, w = im.shape[0], im.shape[1]
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

print(im_gray.shape[::-1])
print(im_gray.shape[1::-1])
# (400, 225)
# (400, 225)
