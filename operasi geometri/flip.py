# Import library OpenCV
import cv2

# Baca gambar dari file
img = cv2.imread("images.jpg")

# Melakukan flip gambar secara horizontal (mirror)
img_flipped = cv2.flip(img, 1)

# Menyimpan gambar yang sudah di-flip
cv2.imwrite("gambar_flipped.jpg", img_flipped)

# Untuk melakukan flip gambar secara vertikal atau menggabungkan flip secara horizontal dan vertikal dapat dilakuka dengan mengganti nilai parameter pada fungsi cv2.flip().