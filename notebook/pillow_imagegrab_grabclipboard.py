from PIL import ImageGrab, Image

img = ImageGrab.grabclipboard()
print(img)
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=200x71 at 0x105E68700>

print(isinstance(img, Image.Image))
# True

print(img.size)
# (200, 71)

print(img.mode)
# RGB

img.save('data/temp/clipboard_image.jpg')

img = ImageGrab.grabclipboard()
print(img)
# None
