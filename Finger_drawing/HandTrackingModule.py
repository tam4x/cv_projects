import cv2
import numpy as np
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectioncon = 0.5, trackingcon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectioncon
        self.trackcon = trackingcon

<<<<<<< HEAD
        self.hand = 0       # 0 für die rechte Hand und 1 für die Linke
=======
>>>>>>> 0bf385e563467213142d0f5a3d2461ba461bf9f2
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

<<<<<<< HEAD

=======
>>>>>>> 0bf385e563467213142d0f5a3d2461ba461bf9f2
    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img   

<<<<<<< HEAD

=======
>>>>>>> 0bf385e563467213142d0f5a3d2461ba461bf9f2
    def line_between_fingers(self, img, line_between_finger: int):
        if self.results.multi_hand_landmarks:
            finger_co = self.findPos(img, 0, draw = False)
            if line_between_finger == 1:
                cv2.line(img, (finger_co[4][1], finger_co[4][2]), (finger_co[8][1], finger_co[8][2]), (0,0,0), 10)
            elif line_between_finger == 2:
                cv2.line(img, (finger_co[8][1], finger_co[8][2]), (finger_co[12][1], finger_co[12][2]), (0,0,0), 10)
            elif line_between_finger == 3:
                cv2.line(img, (finger_co[12][1], finger_co[12][2]), (finger_co[16][1], finger_co[16][2]), (0,0,0), 10)
            elif line_between_finger == 2:
                cv2.line(img, (finger_co[16][1], finger_co[16][2]), (finger_co[20][1], finger_co[20][2]), (0,0,0), 10)

        return img
    
    def findPos(self, img, handno = 0, draw = True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)

        return lmList
<<<<<<< HEAD


    def number_fingers(self, img, lmlist, number_finger : int , finger_pictures = [], draw = True ):
        
=======
    def number_fingers(self, img, lmlist):
>>>>>>> 0bf385e563467213142d0f5a3d2461ba461bf9f2
        fingercups = [4,8,12,16,20]
        finger_count = 0
        finger_pos = []
        finger_number = [0,0,0,0,0]
        for i, finger in enumerate(fingercups):
            
            if len(lmlist) != 0:
                if i!=0:
                    if lmlist[finger][2] < lmlist[finger-2][2]:
                        finger_count += 1
                        finger_pos.append([lmlist[finger][1],lmlist[finger][2]])
                        finger_number[i] = 1
                else:
<<<<<<< HEAD
                    self.detect_left_right(img,lmlist)
                    if self.hand == 1:
                        if lmlist[3][1] > lmlist[4][1]:
                            finger_count +=1
                            finger_pos.append([lmlist[finger][1],lmlist[finger][2]])
                            finger_number[i] = 1
                    else:
                        if lmlist[3][1] < lmlist[4][1]:
                            finger_count +=1
                            finger_pos.append([lmlist[finger][1],lmlist[finger][2]])
                            finger_number[i] = 1
        if draw:
            self.finger_count = finger_pictures
            height, width, c = self.finger_count[0].shape
            if finger_count == 1:
                img[0:width, 0:height] = self.finger_count[0]
            elif finger_count == 2:
                img[0:width, 0:height] = self.finger_count[1]
            elif finger_count == 3:
                img[0:width, 0:height] = self.finger_count[2]
            elif finger_count == 4:
                img[0:width, 0:height] = self.finger_count[3]
            elif finger_count == 5:
                img[0:width, 0:height] = self.finger_count[4]
            elif finger_count == 0:
                img[0:width, 0:height] = self.finger_count[5]


        return finger_count , finger_pos, finger_number, img


    def detect_left_right(self, img, lmlist):
        if lmlist[4][1] < lmlist[0][1]:
            self.hand = 1
        else:
            self.hand = 0

# Bei der rechten Hand hat die Daum ID einen größeren x Wert als der Handmittelpunkt, bei der linken Hand umgekehrt       
=======
                    if lmlist[4][1] < lmlist[3][1]:
                        finger_count +=1
                        finger_pos.append([lmlist[finger][1],lmlist[finger][2]])
                        finger_number[i] = 1
        return finger_count , finger_pos, finger_number
        

        
>>>>>>> 0bf385e563467213142d0f5a3d2461ba461bf9f2
#Linien der Finger in betracht ziehen
            

def main():
    return 0



if __name__ == "__main__":
    main()
