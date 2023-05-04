import numpy as np
import cv2
import mediapipe as mp
import HandTrackingModule as htm
import time


cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img = detector.line_between_fingers(img, 2)
    pos = detector.findPos(img, 0, draw = False)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord("q"):
        break