from my_lib.imagelib import expand2square

from PIL import Image

im = Image.open('data/src/astronaut_rect.bmp')

# ![](data/src/astronaut_rect.bmp)

im_new = expand2square(im, (0, 0, 0))
im_new.save('data/dst/astronaut_expand_square.jpg', quality=95)

# ![](data/dst/astronaut_expand_square.jpg)

im_new = expand2square(im, (0, 0, 0)).resize((150, 150))
