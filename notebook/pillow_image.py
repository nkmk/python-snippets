from PIL import Image, ImageFilter

im = Image.open('data/src/lenna_square.png')

# ![lenna_square](data/src/lenna_square.png)

print(im.format, im.size, im.mode)
# PNG (512, 512) RGB

print(im.getextrema()) 
# ((54, 255), (3, 248), (8, 225))

print(im.getpixel((256, 256)))
# (180, 65, 72)

new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())

new_im.show()

new_im.save('data/dst/lenna_square_pillow.jpg', quality=95)

# ![lenna_square_pillow](data/dst/lenna_square_pillow.jpg)
