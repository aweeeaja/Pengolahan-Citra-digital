from cmath import pi
import cv2
import os
from numpy import full
import numpy as np

# membuat variabel untuk object
# path = os.getcwd()
# gambar = ('contoh 1.jpeg')
# full_path = os.path.join(path, gambar)
# foto = cv2.imread(full_path)

pict = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')
# print(pict)

cv2.imshow('coba' , pict)

# cv2.waitKey()

# memecah channel dengan cara manual
b = pict[:,:,0]
g = pict[:,:,1]
r = pict[:,:,2]

# memecah channel menggunakan fungsi bawaan open cv
# b, g, r = cv2.split(pict)

# membuat matrix baru
gray = np.zeros((len(pict),len(pict[0])))

# Membaca matrix pixel per pixel dan dihitung untuk mengubah ke grayscale
for brs in range (len(pict)):
    for klm in range (len(pict[0])):
        gray[brs,klm] = round(0.299*r[brs,klm]+0.587*g[brs,klm]+0.114*b[brs,klm])

# matrix grayscale dikonversi dari double ke integer
gray = gray.astype(np.uint8)

cv2.imshow("abu", gray)

# menampilkan image manual
cv2.imshow ("blue", pict[:,:,0])
cv2.imshow ("green", pict[:,:,1])
cv2.imshow ("red", pict[:,:,2])

# menampilkan image juga
cv2.imshow ("blue", b)
cv2.imshow ("green", g)
cv2.imshow ("red", r)

cv2.waitKey()

