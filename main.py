import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('ar.png')
# code = decode(img)
# print(code)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:

    Success, img = cap.read()

    for barcode in decode(img):
        print(barcode.data)

        myData = barcode.data.decode('utf-8')
        print(myData)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255), 5)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
