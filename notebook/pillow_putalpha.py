from PIL import Image, ImageDraw, ImageFilter

im_rgb = Image.open('data/src/lena.jpg')

im_rgba = im_rgb.copy()
im_rgba.putalpha(128)
im_rgba.save('data/dst/pillow_putalpha_solid.png')

# ![pillow_putalpha_solid](data/dst/pillow_putalpha_solid.png)

im_a = Image.new("L", im_rgb.size, 0)
draw = ImageDraw.Draw(im_a)
draw.ellipse((140, 50, 260, 170), fill=255)

# ![mask circle](data/dst/mask_circle.jpg)

im_rgba = im_rgb.copy()
im_rgba.putalpha(im_a)
im_rgba_crop = im_rgba.crop((140, 50, 260, 170))
im_rgba_crop.save('data/dst/pillow_putalpha_circle.png')

# ![pillow_putalpha_circle](data/dst/pillow_putalpha_circle.png)

im_a_blur = im_a.filter(ImageFilter.GaussianBlur(4))

# ![mask circle blur](data/dst/mask_circle_blur.jpg)

im_rgba = im_rgb.copy()
im_rgba.putalpha(im_a_blur)
im_rgba_crop = im_rgba.crop((135, 45, 265, 175))
im_rgba_crop.save('data/dst/pillow_putalpha_circle_blur.png')

# ![pillow_putalpha_circle_blur](data/dst/pillow_putalpha_circle_blur.png)

im_a = Image.open('data/src/horse_r.png').convert('L').resize(im_rgb.size)

# ![horse](data/src/horse_r_resize.png)

im_rgba = im_rgb.copy()
im_rgba.putalpha(im_a)
im_rgba.save('data/dst/pillow_putalpha_horse.png')

# ![pillow_putalpha_horse](data/dst/pillow_putalpha_horse.png)
