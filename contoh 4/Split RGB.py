from turtle import color
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


img = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/responsi/5210411097/gambar.jpg')

# b, g, r = cv2.split(img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

jml_brs = len(img)
jml_klm = len(img[0])

biru = np.zeros(256)
hijau = np.zeros(256)
merah = np.zeros(256)

for x in range (jml_brs):
    for y in range (jml_klm):
        pixel_b = b[x,y]
        biru[pixel_b] +=1 / (jml_brs * jml_klm)
        
        pixel_g = g[x,y]
        hijau[pixel_g] +=1 / (jml_brs * jml_klm)
        
        pixel_r = r[x,y]
        merah[pixel_r] +=1 / (jml_brs * jml_klm)

cv2.imshow('gambar', img)
plt.plot(biru, color='blue')
plt.plot(hijau, color='green')
plt.plot(merah, color='red')
plt.show()
cv2.waitKey()