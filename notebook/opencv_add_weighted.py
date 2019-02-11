import cv2

src1 = cv2.imread('data/src/lena.jpg')
src2 = cv2.imread('data/src/rocket.jpg')

src2 = cv2.resize(src2, src1.shape[1::-1])

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

cv2.imwrite('data/dst/opencv_add_weighted.jpg', dst)
# True

# ![](data/dst/opencv_add_weighted.jpg)

dst = cv2.addWeighted(src1, 0.5, src2, 0.2, 128)

cv2.imwrite('data/dst/opencv_add_weighted_gamma.jpg', dst)
# True

# ![](data/dst/opencv_add_weighted_gamma.jpg)
