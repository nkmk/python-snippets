from PIL import Image, ImageFilter

im = Image.open('data/src/lena_square.png')

# ![lena_square](data/src/lena_square.png)

print(im.format, im.size, im.mode)
# PNG (512, 512) RGB

print(im.getextrema()) 
# ((54, 255), (3, 248), (8, 225))

print(im.getpixel((256, 256)))
# (180, 65, 72)

new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())

new_im.show()

new_im.save('data/dst/lena_square_pillow.jpg', quality=95)

# ![lena_square_pillow](data/dst/lena_square_pillow.jpg)
