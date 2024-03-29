import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np 
import math
import time

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands= 1)
offset = 20
imgSize = 300
counter = 0

folder = "C:\Users\vashu\Documents\SignToText\Data\Hello"

while True :
    success , img = cap.read ()
    hands , img = detector.findHands(img)
    if hands : 
        hand =  hands [0]
        x,y,w,h = hand ['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y-offset : y + h + offset , x-offset : x + w + offset]
        imgCropShape = imgCrop.shape