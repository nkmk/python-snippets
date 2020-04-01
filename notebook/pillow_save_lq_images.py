from PIL import Image

img = Image.open('data/src/lena.jpg')

img.save('data/src/lena_q95.jpg', quality=95)
img.save('data/src/lena_q50.jpg', quality=50)
