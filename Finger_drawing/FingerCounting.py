import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm
import ctypes

wcam, hcam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

folderPath = "Fingers/"


myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

resized = [cv2.resize(img, (70,70)) for img in overlayList]



ptime = 0

detector = htm.handDetector(resized)


while True:
    success, img = cap.read()
    
    img = detector.findHands(img)
    lmlist = detector.findPos(img, draw = False)


    count, finger_pos, finger_number,img = detector.number_fingers(img, lmlist, 5, resized)
    

    cTime = time.time()
    fps = 1/(cTime - ptime)
    ptime = cTime

    cv2.putText(img, f'{int(fps)}', (400,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord("q"):
        break
