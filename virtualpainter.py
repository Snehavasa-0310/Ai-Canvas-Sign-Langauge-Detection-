from pathlib import Path

import cv2
import cvzone
import numpy as np
import time
import os
import HandTrackingModule as htm
from cvzone.HandTrackingModule import HandDetector

folderPath = Path("Header")
myList = os.listdir(folderPath)
print(myList)
overlayList =[]
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
while True:

    # 1. Import image
    success, img = cap.read()
    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)






