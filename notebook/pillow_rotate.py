from PIL import Image

im = Image.open('data/src/lena.jpg')

# ![lena](data/src/lena.jpg)

im_rotate = im.rotate(90)
im_rotate.save('data/dst/lena_rotate_90.jpg', quality=95)

# ![lena_rotate_90](data/dst/lena_rotate_90.jpg)

im_rotate = im.rotate(45)
im_rotate.save('data/dst/lena_rotate_45.jpg', quality=95)

# ![lena_rotate_45](data/dst/lena_rotate_45.jpg)

im_rotate = im.rotate(90, expand=True)
im_rotate.save('data/dst/lena_rotate_90_expand.jpg', quality=95)

# ![lena_rotate_90_expand](data/dst/lena_rotate_90_expand.jpg)

im_rotate = im.rotate(45, expand=True)
im_rotate.save('data/dst/lena_rotate_45_expand.jpg', quality=95)

# ![lena_rotate_45_expand](data/dst/lena_rotate_45_expand.jpg)

im_rotate = im.rotate(45, expand=True, resample=Image.BICUBIC)
im_rotate.save('data/dst/lena_rotate_45_expand_bicubic.jpg', quality=95)

# ![lena_rotate_45_expand_bicubic](data/dst/lena_rotate_45_expand_bicubic.jpg)

im_rotate = im.rotate(45, center=(0, 60))
im_rotate.save('data/dst/lena_rotate_45_change_center.jpg', quality=95)

# ![lena_rotate_45_change_center](data/dst/lena_rotate_45_change_center.jpg)

im_rotate = im.rotate(45, center=(0, 60), expand=True)
im_rotate.save('data/dst/lena_rotate_45_change_center_expand.jpg', quality=95)

# ![lena_rotate_45_change_center_expand](data/dst/lena_rotate_45_change_center_expand.jpg)

im_rotate = im.rotate(0, translate=(100, 50))
im_rotate.save('data/dst/lena_rotate_0_translate.jpg', quality=95)

# ![lena_rotate_0_translate](data/dst/lena_rotate_0_translate.jpg)

im_rotate = im.rotate(45, translate=(100, 50))
im_rotate.save('data/dst/lena_rotate_45_translate.jpg', quality=95)

# ![lena_rotate_45_translate](data/dst/lena_rotate_45_translate.jpg)

im_rotate = im.rotate(45, translate=(100, 50), expand=True)
im_rotate.save('data/dst/lena_rotate_45_translate_expand.jpg', quality=95)

# ![lena_rotate_45_translate_expand](data/dst/lena_rotate_45_translate_expand.jpg)
