from my_lib.imagelib import crop_center, crop_max_square

from PIL import Image

im = Image.open('data/src/astronaut_rect.bmp')

# ![](data/src/astronaut_rect.bmp)

im_crop = im.crop((60, 20, 400, 200))
im_crop.save('data/dst/astronaut_pillow_crop.jpg', quality=95)

im.crop((60, 20, 400, 200)).save('data/dst/astronaut_pillow_crop.jpg', quality=95)

# ![](data/dst/astronaut_pillow_crop.jpg)

im_crop_outside = im.crop((200, 150, 600, 360))
im_crop_outside.save('data/dst/astronaut_pillow_crop_outside.jpg', quality=95)

# ![](data/dst/astronaut_pillow_crop_outside.jpg)

im_new = crop_center(im, 300, 150)
im_new.save('data/dst/astronaut_pillow_crop_center.jpg', quality=95)

# ![](data/dst/astronaut_pillow_crop_center.jpg)

im_new = crop_max_square(im)
im_new.save('data/dst/astronaut_pillow_crop_max_square.jpg', quality=95)

# ![](data/dst/astronaut_pillow_crop_max_square.jpg)
