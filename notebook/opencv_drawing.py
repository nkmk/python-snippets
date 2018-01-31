import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0

img = np.full((210, 425, 3), 128, dtype=np.uint8)

cv2.rectangle(img, (50, 10), (125, 60), (255, 0, 0))
cv2.rectangle(img, (50, 80), (125, 130), (0, 255, 0), thickness=-1)
cv2.rectangle(img, (50, 150), (125, 200), (0, 0, 255), thickness=-1)
cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0))

cv2.rectangle(img, (175, 10), (250, 60), (255, 255, 255), thickness=8, lineType=cv2.LINE_4)
cv2.line(img, (175, 10), (250, 60), (0, 0, 0), thickness=1, lineType=cv2.LINE_4)
cv2.rectangle(img, (175, 80), (250, 130), (255, 255, 255), thickness=8, lineType=cv2.LINE_8)
cv2.line(img, (175, 80), (250, 130), (0, 0, 0), thickness=1, lineType=cv2.LINE_8)
cv2.rectangle(img, (175, 150), (250, 200), (255, 255, 255), thickness=8, lineType=cv2.LINE_AA)
cv2.line(img, (175, 150), (250, 200), (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

cv2.rectangle(img, (600, 20), (750, 120), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
cv2.rectangle(img, (601, 160), (751, 260), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
cv2.rectangle(img, (602, 300), (752, 400), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)

cv2.imwrite('data/dst/opencv_draw_argument.png', img)
# True

img_rect = cv2.rectangle(img, (10, 10), (110, 60), (255, 0, 0))
print(img is img_rect)
# True

img = np.full((210, 425, 3), 128, dtype=np.uint8)

cv2.line(img, (50, 10), (125, 60), (255, 0, 0))
cv2.line(img, (50, 60), (125, 10), (0, 255, 255), thickness=4, lineType=cv2.LINE_AA)

cv2.arrowedLine(img, (50, 80), (125, 130), (0, 255, 0), thickness=4)
cv2.arrowedLine(img, (50, 130), (125, 80), (255, 0, 255), tipLength=0.3)

cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0))

cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.ellipse(img, ((190, 105), (20, 50), 0), (255, 255, 255))
cv2.ellipse(img, ((240, 105), (20, 50), 30), (0, 0, 0), thickness=-1)

cv2.ellipse(img, (190, 175), (10, 25), 0, 0, 270, (255, 255, 255))
cv2.ellipse(img, (240, 175), (10, 25), 30, 0, 270, (0, 0, 0), thickness=-1)

cv2.drawMarker(img, (300, 20), (255, 0, 0))
cv2.drawMarker(img, (337, 20), (0, 255, 0), markerType=cv2.MARKER_TILTED_CROSS, markerSize=15)
cv2.drawMarker(img, (375, 20), (0, 0, 255), markerType=cv2.MARKER_STAR, markerSize=10)

cv2.drawMarker(img, (300, 50), (0, 255, 255), markerType=cv2.MARKER_DIAMOND)
cv2.drawMarker(img, (337, 50), (255, 0, 255), markerType=cv2.MARKER_SQUARE, markerSize=15)
cv2.drawMarker(img, (375, 50), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=10)

pts = np.array(((300, 80), (300, 130), (335, 130)))
cv2.polylines(img, [pts], True, (255, 255, 255), thickness=2)

pts = np.array(((335, 80), (375, 80), (375, 130)))
cv2.fillPoly(img, [pts], (0, 0, 0))

cv2.putText(img, 'nkmk', (300, 170), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
cv2.putText(img, 'nkmk', (300, 195), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), lineType=cv2.LINE_AA)

cv2.imwrite('data/dst/opencv_draw_etc.png', img)
# True
