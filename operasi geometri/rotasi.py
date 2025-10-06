# Import library OpenCV
import cv2

# Baca gambar dari file
img = cv2.imread("images.jpg")

# Menentukan titik pusat rotasi dan sudut rotasi (misalnya, rotasi sebesar 180 derajat)
center = (img.shape[1]//2, img.shape[0]//2)
angle = 180

# Melakukan rotasi gambar
M = cv2.getRotationMatrix2D(center, angle, 1.0)
img_rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Menyimpan gambar yang sudah dirotasi
cv2.imshow("gambar_rotated.jpg", img_rotated)
