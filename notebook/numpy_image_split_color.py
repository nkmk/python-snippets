from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

print(im.ndim, im.shape)    # 次元数、サイズ
# => 3 (512, 512, 3)
print(im[256, 256])         # 指定した座標の色（原点は左上）
# => [180  65  72]
print(im[:, :, 0].min())    # Redの最小値
# => 54

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

# 横に並べて結合（どれでもよい）
im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

pil_img = Image.fromarray(im_RGB)
pil_img.save('data/dst/lena_numpy_split_color.jpg')
