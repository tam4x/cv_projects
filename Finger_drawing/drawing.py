import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm
import ctypes


folderpath = "Layouts/"

myList = os.listdir(folderpath)
images = []
for imagepath in myList:
    image = cv2.imread(f"{folderpath}/{imagepath}")
    images.append(image)

images = [cv2.resize(i, (640,120)) for i in images]
header = images[0]

wcam, hcam = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, wcam)
cap.set(4, hcam)

analyse = htm.handDetector()
# Select layouts based in pixel of hand 
# get a selection mode when 2 fingers are up
# get a drawing mode when the index finger is up
# overlay 2 pictures in one, draw on a black image 
# 0:95, 150:200     0:95, 280:350       0:95, 380:460       0:95, 480:600
# select a draw width with a trained neural network for didgets or train it yourself
# make the programm work for both hands
while True:
    success, img = cap.read()

    img = analyse.findHands(img)
    lmlist = analyse.findPos(img, draw = False)

    fingers, pos, finger_number, img = analyse.number_fingers(img, lmlist, 5, draw = False)
    print(pos)

    if finger_number[1] == 1 and finger_number[2] == 1 and fingers == 2: # selection mode
        analyse.line_between_fingers(img, 2)
        # result = cv2.pointPolygonTest(img[0:95, 150:200], (pos[0][1], pos[0][2]), False) 
        # if result ==  1  or  result == 0:
        #    print("is in area")

    if finger_number[1] == 1 and fingers == 1:  #drawing mode
        print(lmlist[8])
        img = cv2.circle(img, (lmlist[8][1], lmlist[8][2]), 5, color = (0,0,0), thickness = cv2.FILLED)
    img[0:120,0:640] = header


    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) == ord("q"):
        break
