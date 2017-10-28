from PIL import Image

img = Image.open('data/src/lena_square.png')

img_resize = img.resize((256, 256))
img_resize.save('data/dst/lena_pillow_resize_nearest.jpg')

img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
img_resize_lanczos.save('data/dst/lena_pillow_resize_lanczos.jpg')

img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
img_resize_lanczos.save('data/dst/lena_pillow_resize_half.jpg')
