import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('ar.png')
# code = decode(img)
# print(code)

for barcode in decode(img):
    print(barcode.polygon)