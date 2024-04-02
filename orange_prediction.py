
import cv2
from orange_detector import OrangeDetector


cap = cv2.VideoCapture("Orange pack without background.mp4")

# Load detector
od = OrangeDetector()


while True:
    ret, frame = cap.read()
    if ret is False:
        break

    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

   
    cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
   


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break