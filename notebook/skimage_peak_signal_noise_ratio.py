import skimage.io
import skimage.metrics

img_org = skimage.io.imread('data/src/lena.jpg')
img_q95 = skimage.io.imread('data/src/lena_q95.jpg')
img_q50 = skimage.io.imread('data/src/lena_q50.jpg')

print(skimage.metrics.peak_signal_noise_ratio(img_org, img_q95))
# 39.024557583745676

print(skimage.metrics.peak_signal_noise_ratio(img_org, img_q50))
# 30.34829234238757

print(skimage.metrics.peak_signal_noise_ratio(img_org, img_org))
# inf
# 
# /usr/local/lib/python3.7/site-packages/skimage/metrics/simple_metrics.py:160: RuntimeWarning: divide by zero encountered in double_scalars
#   return 10 * np.log10((data_range ** 2) / err)

print(skimage.metrics.peak_signal_noise_ratio(img_org, img_q95, data_range=255))
# 39.024557583745676
