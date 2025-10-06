# Import library OpenCV
import cv2

# Baca gambar dari file
img = cv2.imread("images.jpg")

# Scaling gambar menjadi ukuran yang lebih kecil (misalnya, 50% dari ukuran asli)
# Untuk mengubah ukuran scaling caranya dengan mengubah nilai fx dan fy dalam fungsi cv2.resize().
img_scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

# Menyimpan gambar yang sudah di-scaling
cv2.imwrite("gambar_scaled.jpg", img_scaled)

