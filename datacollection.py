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