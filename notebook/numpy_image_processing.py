from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

print(im.dtype)  # データ型
# uint8

print(im.ndim)  # 次元数
# 3

print(im.shape)  # サイズ（高さ x 幅 x 色数）
# (512, 512, 3)

im_f = np.array(Image.open('data/src/lena_square.png'), 'f')

print(im_f.dtype)  # データ型
# float32

print(im[256, 256])  # 指定した座標の画素値（R, G, B） / 原点は左上
# [180  65  72]

print(im[:, :, 0].min())  # Redの最小値
# 54

pil_img = Image.fromarray(im)
pil_img.save('data/dst/lena_square_save.png')

Image.fromarray(im).save('data/dst/lena_square_save.png')

pil_img_f = Image.fromarray(np.uint8(im_f))
pil_img_f.save('data/dst/lena_square_save.png')
