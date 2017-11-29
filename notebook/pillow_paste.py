from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('data/src/rocket.jpg')
im2 = Image.open('data/src/lena.jpg')

# ![rocket](data/src/rocket.jpg)
# ![lena](data/src/lena.jpg)

im1.paste(im2)
im1.save('data/dst/rocket_pillow_paste.jpg', quality=95)

# ![rocket_pillow_paste](data/dst/rocket_pillow_paste.jpg)

im1 = Image.open('data/src/rocket.jpg')
im2 = Image.open('data/src/lena.jpg')

back_im = im1.copy()
back_im.paste(im2)
back_im.save('data/dst/rocket_pillow_paste.jpg', quality=95)

back_im = im1.copy()
back_im.paste(im2, (100, 50))
back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)

# ![rocket_pillow_paste_pos](data/dst/rocket_pillow_paste_pos.jpg)

back_im = im1.copy()
back_im.paste(im2, (400, 100))
back_im.save('data/dst/rocket_pillow_paste_out.jpg', quality=95)

# ![rocket_pillow_paste_out](data/dst/rocket_pillow_paste_out.jpg)

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((140, 50, 260, 170), fill=255)
mask_im.save('data/dst/mask_circle.jpg', quality=95)

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im)
back_im.save('data/dst/rocket_pillow_paste_mask_circle.jpg', quality=95)

# ![rocket_pillow_paste_mask_circle](data/dst/rocket_pillow_paste_mask_circle.jpg)

mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save('data/dst/mask_circle_blur.jpg', quality=5)

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im_blur)
back_im.save('data/dst/rocket_pillow_paste_mask_circle_blur.jpg', quality=95)

# ![rocket_pillow_paste_mask_circle_blur](data/dst/rocket_pillow_paste_mask_circle_blur.jpg)

mask_im = Image.open('data/src/horse.png').resize(im2.size).convert('L')

back_im = im1.copy()
back_im.paste(im2, (100, 50), mask_im)
back_im.save('data/dst/rocket_pillow_paste_mask_horse.jpg', quality=95)

# ![rocket_pillow_paste_mask_horse](data/dst/rocket_pillow_paste_mask_horse.jpg)
