import cv2
import numpy as np


img = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/responsi/5210411097/gambar.jpg')

b, g, r = cv2.split(img)

jml_baris = len(img)
jml_kolom = len(img[0])
biru = np.zeros(256)
green = np.zeros(256)
red = np.zeros(256)

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

abu_brightness = np.zeros((len(abu),len(abu[0])))

for brs in range (len(abu)):
    for klm in range (len(abu[0])):
        abu_brightness[brs,klm] = abu[brs,klm] + 30 
        if abu_brightness[brs,klm] > 255:
            abu_brightness[brs,klm] = 255

abu_brightness = abu_brightness.astype(np.uint8)

binary = np.zeros((len(abu_brightness),len(abu_brightness[0])))
tresh = 160

for brs in range (len(abu_brightness)):
    for klm in range (len(abu_brightness[0])):
        if abu_brightness[brs,klm]>= 160:
            binary[brs,klm]=1
        else:
            binary[brs,klm]=0

cv2.imshow('hitamputih', binary)
cv2.imshow('no4', abu_brightness)
cv2.waitKey()

# function bawaan open cv
image = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/responsi/5210411097/gambar.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2],image.dtype)*30
#operasi penjumlahan
citraPenjumlahan = cv2.add(gray,MatriksSatu)

ret,bw = cv2.threshold(citraPenjumlahan, 160, 255, cv2.THRESH_BINARY)

cv2.imshow('Citra Penjumlahan', citraPenjumlahan)
cv2.imshow('hitamputih', bw)
cv2.waitKey()