import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm
import ctypes


folderpath = "Layouts/"

myList = os.listdir(folderpath)
images = []
myList.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

for imagepath in myList:
    image = cv2.imread(f"{folderpath}/{imagepath}")
    images.append(image)

images = [cv2.resize(i, (640,120)) for i in images]
wcam, hcam = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, wcam)
cap.set(4, hcam)

analyse = htm.handDetector()
# Select layouts based in pixel of hand 
# get a selection mode when 2 fingers are up
# get a drawing mode when the index finger is up
# overlay 2 pictures in one, draw on a black image
#height:width, height:width or y,x y,x fingers are detected in x,y or width,height
# 0:135, 120:230     0:250, 120:350      0:370, 120:460       0:500, 120:600
# select a draw width with a trained neural network for didgets or train it yourself
# make the programm work for both hands
while True:
    success, img = cap.read()
    img[0:120,0:640] = images[analyse.mode]

    img = analyse.findHands(img)
    lmlist = analyse.findPos(img, draw = False)

    fingers, pos, finger_number, img = analyse.number_fingers(img, lmlist, 5, draw = False)
    print(pos)

    if finger_number[1] == 1 and finger_number[2] == 1 and fingers == 2 and abs((pos[0][0] - pos[1][0])) < 30: # selection mode
        analyse.line_between_fingers(img, 2)
        analyse.select_mode(pos)

    if finger_number[1] == 1 and fingers == 1:  #drawing mode
        
        img = cv2.circle(img, (lmlist[8][1], lmlist[8][2]), 5, color = (0,0,0), thickness = cv2.FILLED)

        

    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) == ord("q"):
        break
