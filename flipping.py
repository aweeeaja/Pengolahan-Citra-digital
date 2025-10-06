import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

flip_hz = 1
flip_vt = 0

matrix_baru  = np.zeros((jml_baris, jml_kolom, 3))

for brs in range (jml_baris):
    for klm in range (jml_kolom):
        
        if(flip_hz == 1):
            klm_baru = jml_kolom - klm -1
        else :
            klm_baru = klm

        if(flip_vt == 1):
            brs_baru = jml_baris - brs -1
        else:
            brs_baru = brs
      
        matrix_baru[brs_baru,klm_baru] = gambar[brs,klm]

        

matrix_baru = matrix_baru.astype(np.uint8)


cv2.imshow("gambar",gambar)
cv2.imshow("abu", matrix_baru)
cv2.waitKey()