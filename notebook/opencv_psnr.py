import cv2

img_org = cv2.imread('data/src/lena.jpg')
img_q95 = cv2.imread('data/src/lena_q95.jpg')
img_q50 = cv2.imread('data/src/lena_q50.jpg')

print(cv2.PSNR(img_org, img_q95))
# 39.02455758374567

print(cv2.PSNR(img_org, img_q50))
# 30.34829234238757

print(cv2.PSNR(img_org, img_org))
# 361.20199909921956

print(cv2.PSNR(img_org, img_q95, R=255))
# 39.02455758374567
