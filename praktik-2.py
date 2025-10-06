import cv2
from cv2 import THRESH_BINARY
from numpy import full
import numpy as np

pict = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

gray = cv2.cvtColor(pict, cv2.COLOR_BGR2GRAY)

# ret,bw = cv2.threshold(gray,157,255,cv2.THRESH_BINARY)

binary = np.zeros((len(gray),len(gray[0])))

for brs in range (len(gray)):
    for klm in range (len(gray[0])):
        if binary[brs,klm]>125:
            binary[brs,klm]=1
        else:
            binary[brs,klm]=0



cv2.imshow("RGB", pict)
cv2.imshow("GRAY", gray)
cv2.imshow("bw", binary)
cv2.waitKey()