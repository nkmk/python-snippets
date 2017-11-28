from PIL import Image

im = Image.open('data/src/lena_square.png')

# ![lena_square](data/src/lena_square.png)

im_crop = im.crop((100, 200, 400, 300))
im_crop.save('data/dst/lena_square_pillow_crop.jpg', quality=95)

im.crop((100, 200, 400, 300)).save('data/dst/lena_square_pillow_crop.jpg', quality=95)

# ![lena_square_pillow_crop](data/dst/lena_square_pillow_crop.jpg)

im_crop_outside = im.crop((300, 300, 600, 600))
im_crop_outside.save('data/dst/lena_square_pillow_crop_outside.jpg', quality=95)

# ![lena_square_pillow_crop_outside](data/dst/lena_square_pillow_crop_outside.jpg)

def crop_center(pil_img, width, height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - width) / 2,
                         (img_height - height) / 2,
                         (img_width + width) / 2,
                         (img_height + height) / 2))

im_crop_center = crop_center(im, 200, 200)
im_crop_center.save('data/dst/lena_square_pillow_crop_center.jpg', quality=95)

# ![lena_square_pillow_crop_center](data/dst/lena_square_pillow_crop_center.jpg)
