from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('data/src/lena.jpg')
im2 = Image.open('data/src/rocket.jpg').resize(im1.size)

im2.save('data/src/rocket_resize.jpg')

# ![lena](data/src/lena.jpg)
# ![rocket_resize](data/src/rocket_resize.jpg)

mask = Image.new("L", im1.size, 128)
im = Image.composite(im1, im2, mask)
# im = Image.blend(im1, im2, 0.5)

im.save('data/dst/pillow_composite_solid.jpg', quality=95)

# ![pillow_composite_solid](data/dst/pillow_composite_solid.jpg)

mask = Image.new("L", im1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((140, 50, 260, 170), fill=255)
im = Image.composite(im1, im2, mask)

im.save('data/dst/pillow_composite_circle.jpg', quality=95)

# ![pillow_composite_circle](data/dst/pillow_composite_circle.jpg)

mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
im = Image.composite(im1, im2, mask_blur)

im.save('data/dst/pillow_composite_circle_blur.jpg', quality=95)

# ![pillow_composite_circle_blur](data/dst/pillow_composite_circle_blur.jpg)

mask = Image.open('data/src/horse.png').convert('L').resize(im1.size)
im = Image.composite(im1, im2, mask)

im.save('data/dst/pillow_composite_horse.jpg', quality=95)

# ![pillow_composite_horse](data/dst/pillow_composite_horse.jpg)

mask = Image.open('data/src/gradation_h.jpg').convert('L').resize(im1.size)
im = Image.composite(im1, im2, mask)

im.save('data/dst/pillow_composite_gradation.jpg', quality=95)

# ![pillow_composite_gradation](data/dst/pillow_composite_gradation.jpg)
