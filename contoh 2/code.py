import cv2
import numpy as np
import matplotlib.pyplot as plt

pict = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/contoh 2/gambar.jpg')

# 1. Rotasi Gambar

jml_brs = len(pict)
jml_klm = len(pict[0])

rotasi = -5
rotasi_rad = 22/7 * rotasi / 180

matrix = np.zeros ((jml_brs, jml_klm, 3))

pivot_brs = round(jml_brs/2)
pivot_klm = round(jml_klm/2)

for brs_baru in range (jml_brs):
    for klm_baru in range (jml_klm):

        brs = pivot_brs + (brs_baru - pivot_brs)*np.cos(rotasi_rad) - (klm_baru - pivot_klm)*np.sin(rotasi_rad)
        klm = pivot_klm + (brs_baru - pivot_brs)*np.sin(rotasi_rad) + (klm_baru -pivot_klm)*np.cos(rotasi_rad)

        brs = round (brs)
        klm = round (klm)

        if (brs < jml_brs and brs > 0):
            if (klm < jml_klm and klm > 0):
                matrix[brs_baru,klm_baru] = pict[brs,klm]

matrix = matrix.astype(np.uint8)

# menggunakan fungsi open cv
center = (pict.shape[1]//2, pict.shape[0]//2)
angle = 180

M = cv2.getRotationMatrix2D(center, angle, 1.0)
img_rotated = cv2.warpAffine(pict, M, (pict.shape[1], pict.shape[0]))



# 2. menerangkan gambar

#menggunakan open cv

gray = cv2.cvtColor(matrix, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(matrix.shape[:2],matrix.dtype)*100
#operasi penjumlahan
citraPenjumlahan = cv2.add(gray,MatriksSatu)

# 3. pertajam gambar

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])    #sharp

#konversi ke grayscale

matriks_baru = np.zeros((jml_brs, jml_klm))

#loop mulai dari pixel (1,1)
for brs in range(1,jml_brs-1):
    for klm in range(1,jml_klm-1):
        #baca dan kalikan matriks 3x3 dari gambar awal dengan kernel 3x3
        a = citraPenjumlahan[brs-1,klm-1] * kernel[0,0]   #kiri atas
        b = citraPenjumlahan[brs-1,klm] * kernel[0,1]     #tengah atas
        c = citraPenjumlahan[brs-1,klm+1] * kernel[0,2]   #kanan atas
        d = citraPenjumlahan[brs,klm-1] * kernel[1,0]     #kiri
        e = citraPenjumlahan[brs,klm] * kernel[1,1]       #tengah matriks
        f = citraPenjumlahan[brs,klm+1] * kernel[1,2]     #kanan
        g = citraPenjumlahan[brs+1,klm-1] * kernel[2,0]   #kiri bawah
        h = citraPenjumlahan[brs+1,klm] * kernel[2,1]     #tengah bawah
        i = citraPenjumlahan[brs+1,klm+1] * kernel[2,2]   #kanan bawah

        #hitung total nilai dalam kernel
        jum_kernel = np.sum(kernel)
        if (jum_kernel == 0):
            jum_kernel = 1

        #hitung hasil konvolusi
        konvolusi = np.round((a + b + c + d + e + f + g + h + i) / jum_kernel)

        #perbaiki hasil konvolusi jika di luar rentang 0-255
        if (konvolusi < 0):
            konvolusi = 0
        
        if (konvolusi > 255):
            konvolusi = 255

        #isikan hasil konvolusi ke matriks_baru
        matriks_baru[brs, klm] = konvolusi

#konversi citra_translasi menjadi uint8
matriks_baru = matriks_baru.astype(np.uint8)

# open cv

pertajam = cv2.filter2D(src=citraPenjumlahan, ddepth=-1, kernel=kernel)


cv2.imshow('asli', pict)
cv2.imshow('hasil', matriks_baru)
cv2.imshow('hasil2', pertajam)
cv2.waitKey()