from PIL import Image, ImageOps

im = Image.open('data/src/lena.jpg')
im_invert = ImageOps.invert(im)
im_invert.save('data/dst/lena_invert.jpg', quality=95)

# ![lena](data/src/lena.jpg)
# ![lena_invert](data/dst/lena_invert.jpg)

im = Image.open('data/src/horse.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('data/dst/horse_invert.png')

# ![horse_invert](data/src/horse.png)
# ![horse_invert](data/dst/horse_invert.png)
