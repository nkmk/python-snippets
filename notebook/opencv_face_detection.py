import cv2

img = cv2.imread('data/src/lenna_square.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(type(img), img.shape)
print(type(img_gray), img_gray.shape)
# <class 'numpy.ndarray'> (512, 512, 3)
# <class 'numpy.ndarray'> (512, 512)

cascade_path = '/usr/local/Cellar/opencv3/3.2.0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_path)

faces = cascade.detectMultiScale(img_gray)

print(faces)
# [[215 201 175 175]]

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imwrite('data/dst/lenna_square_face.jpg', img)
# True
