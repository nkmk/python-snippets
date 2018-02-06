from PIL import Image

im = Image.open('data/src/lena.jpg')

print(im.size)
print(type(im.size))
# (400, 225)
# <class 'tuple'>

w, h = im.size
print('width: ', w)
print('height:', h)
# width:  400
# height: 225

print('width: ', im.width)
print('height:', im.height)
# width:  400
# height: 225

im_gray = Image.open('data/src/lena.jpg').convert('L')

print(im.size)
print('width: ', im.width)
print('height:', im.height)
# (400, 225)
# width:  400
# height: 225
