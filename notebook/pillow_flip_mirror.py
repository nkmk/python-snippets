from PIL import Image, ImageOps

im = Image.open('data/src/lena.jpg')

# ![lena](data/src/lena.jpg)

im_flip = ImageOps.flip(im)
im_flip.save('data/dst/lena_flip.jpg', quality=95)

# ![lena_flip](data/dst/lena_flip.jpg)

im_mirror = ImageOps.mirror(im)
im_mirror.save('data/dst/lena_mirror.jpg', quality=95)

# ![lena_mirror](data/dst/lena_mirror.jpg)

im = Image.open('data/src/horse.png')

# ![horse](data/src/horse.png)

im_flip = ImageOps.flip(im)
im_flip.save('data/dst/horse_flip.png', quality=95)

# ![horse_flip](data/dst/horse_flip.png)

im_mirror = ImageOps.mirror(im)
im_mirror.save('data/dst/horse_mirror.png', quality=95)

# ![horse_mirror](data/dst/horse_mirror.png)
