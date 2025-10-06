import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

skala = 2

brs_baru = round(jml_baris*skala)
klm_baru = round(jml_kolom*skala)
matrix_baru = np.zeros((brs_baru, klm_baru, 3))

for x in range (brs_baru):
    for y in range (klm_baru):
        
        brs = int(x / skala)
        klm = int(y / skala)

        matrix_baru[x,y] = gambar[brs,klm]

matrix_baru = matrix_baru.astype(np.uint8)
cv2.imshow("gambar",gambar)
cv2.imshow("abu", matrix_baru)
cv2.waitKey()