import cv2
import numpy as np


img = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/responsi/5210411097/gambar.jpg')

b = img [:,:,0]
g = img [:,:,1]
r = img [:,:,2]

jml_brs = len(img)
jml_klm = len(img[0])

abu = np.zeros((len(img),len(img[0])))

# Membaca matrix pixel per pixel dan dihitung untuk mengubah ke grayscale
for brs in range (jml_brs):
    for klm in range (jml_klm):
        abu[brs,klm] = round(0.299*r[brs,klm]+0.587*g[brs,klm]+0.114*b[brs,klm])
    
abu = abu.astype(np.uint8)

cv2.imshow('gambar', img)
cv2.imshow('grayscale', abu)
cv2.waitKey()
