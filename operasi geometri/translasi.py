# Import library OpenCV dan Numpy
import cv2
import numpy as np

# Baca gambar dari file
img = cv2.imread("images.jpg")

# Menentukan jarak translasi pada sumbu x dan y (misalnya, 100 piksel ke kanan dan 50 piksel ke bawah)
# Untuk mengubah jarak translasi caranya dengan mengubah nilai shift_x dan shift_y.
shift_x = 100
shift_y = 50

# Melakukan translasi gambar
M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
img_translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Menyimpan gambar yang sudah ditranslasi
cv2.imwrite("gambar_translated.jpg", img_translated)
