import cv2
import numpy as np

img = cv2.imread("D:/file adit/tugas kuliah/sem 3/PCD Praktik/contoh 3/Bunga_Mawar_Merah.jpg")

jml_brs = len(img)
jml_klm = len(img[0])

skala = 1.5

brs_baru = round (jml_brs*skala)
klm_baru = round (jml_klm*skala)
perbesar = np.zeros((brs_baru,klm_baru,3))

for x in range(brs_baru):
    for y in range (klm_baru):
        brs = int(x / skala)
        klm = int(y / skala)

        perbesar [x,y] = img [brs,klm]

jml_baris = len(perbesar)
jml_kolom = len (perbesar[0])

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])    #sharp

pertajam = np.zeros((jml_baris,jml_kolom,3))

for brs in range(1,jml_baris-1):
    for klm in range(1,jml_kolom-1):
        for ch in range (3):
            a = perbesar[brs-1,klm-1,ch] * kernel[0,0]   
            b = perbesar[brs-1,klm,ch] * kernel[0,1]     
            c = perbesar[brs-1,klm+1,ch] * kernel[0,2]   
            d = perbesar[brs,klm-1,ch] * kernel[1,0]     
            e = perbesar[brs,klm,ch] * kernel[1,1]       
            f = perbesar[brs,klm+1,ch] * kernel[1,2]     
            g = perbesar[brs+1,klm-1,ch] * kernel[2,0]   
            h = perbesar[brs+1,klm,ch] * kernel[2,1]     
            i = perbesar[brs+1,klm+1,ch] * kernel[2,2]   

            jum_kernel = np.sum(kernel)
            if (jum_kernel == 0):
                jum_kernel = 1

            konvolusi = np.round((a + b + c + d + e + f + g + h + i) / jum_kernel)

            if (konvolusi < 0):
                konvolusi = 0
            
            if (konvolusi > 255):
                konvolusi = 255

            pertajam[brs, klm,ch] = konvolusi

jum_brs = len(pertajam)
jum_klm = len(pertajam[0])

for i in range (jum_brs):
    for j in range (jum_klm):
        (b,g,r) = pertajam [i,j]

        pertajam[i,j] = (b+20, g+20, r-30)

perbesar = perbesar.astype(np.uint8)
pertajam = pertajam.astype(np.uint8)
cv2.imshow ("asli",img)
cv2.imshow ('pertajam',pertajam)
cv2.waitKey()