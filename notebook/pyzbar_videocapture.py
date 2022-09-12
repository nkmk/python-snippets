import cv2
from pyzbar.pyzbar import decode

camera_id = 0
delay = 1
window_name = 'OpenCV pyzbar'

cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        for d in decode(frame):
            s = d.data.decode()
            print(s)
            frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                  (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
            frame = cv2.putText(frame, s, (d.rect.left, d.rect.top + d.rect.height),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
