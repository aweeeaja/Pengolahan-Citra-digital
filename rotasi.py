import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

rotasi = -45
rotasi_rad = 22/7 * rotasi / 180

matrix_baru = np.zeros((jml_baris, jml_kolom, 3))

pivot_brs = round(jml_baris/2)
pivot_klm = round(jml_kolom/2)

for brs in range (jml_baris):
    for klm in range (jml_kolom):

        brs_baru = pivot_brs + (brs - pivot_brs)*np.cos(rotasi_rad) - (klm - pivot_klm)*np.sin(rotasi_rad)
        klm_baru = pivot_klm + (brs - pivot_brs)*np.sin(rotasi_rad) + (klm -pivot_klm)*np.cos(rotasi_rad)

        brs_baru = round (brs_baru)
        klm_baru = round (klm_baru)

        if (brs_baru < jml_baris and brs_baru > 0):
            if (klm_baru < jml_kolom and klm_baru > 0):
                matrix_baru[brs_baru,klm_baru] = gambar[brs,klm]

matrix_baru = matrix_baru.astype(np.uint8)
cv2.imshow("gambar",gambar)
cv2.imshow("abu", matrix_baru)
cv2.waitKey()