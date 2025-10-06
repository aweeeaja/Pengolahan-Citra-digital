import cv2
import numpy as np


image = cv2.imread("images.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2],image.dtype)*5
#operasi perkalian
citraperkalian = cv2.multiply(gray,MatriksSatu)
cv2.imshow('Citra', gray)
cv2.imshow('Citra Penjumlahan', citraperkalian)
cv2.waitKey(0)