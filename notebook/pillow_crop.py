from PIL import Image

im = Image.open('data/src/lena.jpg')

# ![lena](data/src/lena.jpg)

im_crop = im.crop((100, 75, 300, 150))
im_crop.save('data/dst/lena_pillow_crop.jpg', quality=95)

im.crop((100, 75, 300, 150)).save('data/dst/lena_pillow_crop.jpg', quality=95)

# ![lena_pillow_crop](data/dst/lena_pillow_crop.jpg)

im_crop_outside = im.crop((100, 175, 300, 250))
im_crop_outside.save('data/dst/lena_pillow_crop_outside.jpg', quality=95)

# ![lena_pillow_crop_outside](data/dst/lena_pillow_crop_outside.jpg)
