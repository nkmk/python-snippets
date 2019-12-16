import skimage.io
import skimage.util

a = skimage.io.imread('data/src/lena.jpg')
print(a.shape)
# (225, 400, 3)

b = a // 2
c = a // 3

m = skimage.util.montage([a, b, c], multichannel=True)
print(m.shape)
# (450, 800, 3)

skimage.io.imsave('data/dst/skimage_montage_default.jpg', m)

# skimage.util.montage([a, b, c])
# ValueError: Input array has to be either 3- or 4-dimensional

m_fill = skimage.util.montage([a, b, c], fill=(255, 128, 0), multichannel=True)

skimage.io.imsave('data/dst/skimage_montage_fill.jpg', m_fill)

m_1_3_pad = skimage.util.montage([a, b, c],
                                 fill=(0, 0, 0),
                                 grid_shape=(1, 3),
                                 padding_width=10,
                                 multichannel=True)

print(m_1_3_pad.shape)
# (245, 1240, 3)

skimage.io.imsave('data/dst/skimage_montage_1_3_pad.jpg', m_1_3_pad)
