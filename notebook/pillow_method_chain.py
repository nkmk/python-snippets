from PIL import Image, ImageFilter

im = Image.open('data/src/lena_square.png')
im = im.convert('L')
im = im.rotate(90)
im = im.filter(ImageFilter.GaussianBlur())
im.save('data/temp/lena_square_pillow.jpg', quality=95)

Image.open('data/src/lena_square.png').convert('L').rotate(90).filter(ImageFilter.GaussianBlur()).save('data/temp/lena_square_pillow.jpg', quality=95)

(
    Image.open('data/src/lena_square.png')
    .convert('L')
    .rotate(90)
    .filter(ImageFilter.GaussianBlur())
    .save('data/temp/lena_square_pillow.jpg', quality=95)
)

Image.open('data/src/lena_square.png').convert('L').rotate(90).filter(
    ImageFilter.GaussianBlur()
).save('data/temp/lena_square_pillow.jpg', quality=95)
