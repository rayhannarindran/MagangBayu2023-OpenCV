import cv2 as cv
import numpy as np

# Membaca Gambarnya
image = cv.imread("Mochammad Gery Tauristino_5024221048_TugasOpenCV/Tugas3/tugas3.jpg")
img = image
# Menampilakn Gambar original
cv.imshow("Original", image)

# Mencari pinggiran pada gambar menggunakan algoritma canny
canny = cv.Canny(img, 100, 200)

# Mencari Contour
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# MEnggambar contournya
cv.drawContours(img, contours, 2, (0, 0, 0), 3)

# Mencari Berapa banyak sisi dari contournya
peri = cv.arcLength(contours[2], True)
approx = cv.approxPolyDP(contours[2], 0.02 * peri, True)
cv.putText(img, str(len(approx)), (20, 70), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

# Menampilkan Gambar yang sudah diedit
cv.imshow("Hasil", img)
cv.imwrite("tugas3_done.jpg",img)

cv.waitKey(0)
cv.destroyAllWindows()
