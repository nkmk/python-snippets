import cv2

src1 = cv2.imread('data/src/lena.jpg')

src2 = cv2.imread('data/src/horse_r.png')

src2 = cv2.resize(src2, src1.shape[1::-1])

print(src2.shape)
# (225, 400, 3)

print(src2.dtype)
# uint8

dst = cv2.bitwise_and(src1, src2)

cv2.imwrite('data/dst/opencv_bitwise_and.jpg', dst)
# True

# ![](data/dst/opencv_bitwise_and.jpg)
