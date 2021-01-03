from my_lib.imagelib import crop_center, crop_max_square, expand2square, mask_circle_solid, mask_circle_transparent

import os
import glob

from PIL import Image, ImageDraw, ImageFilter

im = Image.open('data/src/astronaut_rect.bmp')
thumb_width = 200

# ![](data/src/astronaut_rect.bmp)

im_thumb = crop_center(im, thumb_width, thumb_width)
im_thumb.save('data/dst/astronaut_thumbnail_center_square.jpg', quality=95)

# ![](data/dst/astronaut_thumbnail_center_square.jpg)

im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
im_thumb.save('data/dst/astronaut_thumbnail_max_square.jpg', quality=95)

# ![](data/dst/astronaut_thumbnail_max_square.jpg)

im_thumb = expand2square(im, (0, 0, 0)).resize((thumb_width, thumb_width), Image.LANCZOS)
im_thumb.save('data/dst/astronaut_thumbnail_expand.jpg', quality=95)

# ![](data/dst/astronaut_thumbnail_expand.jpg)

im_square = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
im_thumb = mask_circle_solid(im_square, (0, 0, 0), 4)
im_thumb.save('data/dst/astronaut_thumbnail_mask_circle_solid.jpg', quality=95)

# ![](data/dst/astronaut_thumbnail_mask_circle_solid.jpg)

im_square = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
im_thumb = mask_circle_transparent(im_square, 4)
im_thumb.save('data/dst/astronaut_thumbnail_mask_circle_transparent.png')

# ![](data/dst/astronaut_thumbnail_mask_circle_transparent.png)

src_dir = 'data/temp/src'
dst_dir = 'data/temp/dst'

files = glob.glob(os.path.join(src_dir, '*.jpg'))

for f in files:
    im = Image.open(f)
    im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
    ftitle, fext = os.path.splitext(os.path.basename(f))
    im_thumb.save(os.path.join(dst_dir, ftitle + '_thumbnail' + fext), quality=95)
