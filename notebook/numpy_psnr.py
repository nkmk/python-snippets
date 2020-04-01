import numpy as np
import cv2

def psnr(img_1, img_2, data_range=255):
    mse = np.mean((img_1.astype(float) - img_2.astype(float)) ** 2)
    return 10 * np.log10((data_range ** 2) / mse)

img_org = cv2.imread('data/src/lena.jpg')
img_q95 = cv2.imread('data/src/lena_q95.jpg')
img_q50 = cv2.imread('data/src/lena_q50.jpg')

print(psnr(img_org, img_q95))
# 39.024557583745676

print(psnr(img_org, img_q50))
# 30.34829234238757

print(psnr(img_org, img_org))
# inf
# 
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:3: RuntimeWarning: divide by zero encountered in double_scalars
#   This is separate from the ipykernel package so we can avoid doing imports until
