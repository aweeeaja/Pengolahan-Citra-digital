from turtle import color
import cv2
import numpy as np
import matplotlib.pyplot as plt

pict = cv2.imread('D:/file adit/tugas kuliah/sem 3/PCD Praktik/images.jpg')

b, g, r = cv2.split(pict)

jml_baris = len(pict)
jml_kolom = len(pict[0])
biru = np.zeros(256)
green = np.zeros(256)
red = np.zeros(256)

for brs in range (len(b)):
    for klm in range (len(b[0])):
        pixel_b = b[brs,klm]
        biru[pixel_b] +=1 / (jml_baris * jml_kolom)
        
        pixel_g = g[brs,klm]
        green[pixel_g] +=1 / (jml_baris * jml_kolom)
        
        pixel_r = r[brs,klm]
        red[pixel_r] +=1 / (jml_baris * jml_kolom)

# print (biru)

g = cv2.cvtColor(pict, cv2.COLOR_BGR2GRAY)

gray = np.zeros(256)

for i in range (len(g)):
    for j in range (len(g[0])):
        pixel_g = g[i,j]
        gray[pixel_g] +=1

cv2.imshow("gambar",pict)
cv2.imshow("abu", g)
cv2.imshow("gray", g)
plt.plot(biru, color='blue')
plt.plot(green, color='green')
plt.plot(red, color='red')
# plt.plot(gray, color='gray')
plt.show()
cv2.waitKey()

# pr Histogram grayscale
