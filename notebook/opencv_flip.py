import cv2

img = cv2.imread('data/src/lena.jpg')
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

img_flip_ud = cv2.flip(img, 0)
cv2.imwrite('data/dst/lena_cv_flip_ud.jpg', img_flip_ud)
# True

img_flip_lr = cv2.flip(img, 1)
cv2.imwrite('data/dst/lena_cv_flip_lr.jpg', img_flip_lr)
# True

img_flip_ud_lr = cv2.flip(img, -1)
cv2.imwrite('data/dst/lena_cv_flip_ud_lr.jpg', img_flip_ud_lr)
# True
