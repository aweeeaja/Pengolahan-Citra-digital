import cv2

import numpy as np

#citra input adalah citra RGB

image = cv2.imread("images.jpg") 

#konversi RGB ke Grayscale

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#Buat matriks 255 seukuran dengan citra

Matriks = np.ones(image.shape[:2],image.dtype)*255 

#Operasi citra negatif

citraNegatif = Matriks - gray 

cv2.imshow('Citra', gray)

cv2.imshow('Citra negatif', citraNegatif) 

cv2.waitKey(0)



