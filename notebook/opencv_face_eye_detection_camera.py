import cv2

face_cascade_path = '/usr/local/opt/opencv/share/'\
                    'OpenCV/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/usr/local/opt/opencv/share/'\
                   'OpenCV/haarcascades/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = img[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('video image', img)
    key = cv2.waitKey(10)
    if key == 27:  # ESCキーで終了
        break

cap.release()
cv2.destroyAllWindows()
