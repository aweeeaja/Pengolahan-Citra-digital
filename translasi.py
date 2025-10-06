import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

geser_hz = 100
geser_vt = -50

matrix_baru  = np.zeros((jml_baris, jml_kolom, 3))

for brs in range (jml_baris):
    for klm in range (jml_kolom):
        brs_baru = brs + geser_vt
        klm_baru = klm + geser_hz

        if(klm_baru < jml_kolom and klm_baru > 0):
            if(brs_baru < jml_baris and brs_baru >0):
                matrix_baru[brs_baru,klm_baru] = gambar[brs,klm]

        

matrix_baru = matrix_baru.astype(np.uint8)


cv2.imshow("gambar",gambar)
cv2.imshow("abu", matrix_baru)
cv2.waitKey()