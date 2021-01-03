from my_lib.imagelib import add_margin

from PIL import Image

im = Image.open('data/src/astronaut_rect.bmp')

# ![](data/src/astronaut_rect.bmp)

im_new = add_margin(im, 50, 10, 0, 100, (128, 0, 64))
im_new.save('data/dst/astronaut_add_margin.jpg', quality=95)

# ![](data/dst/astronaut_add_margin.jpg)
