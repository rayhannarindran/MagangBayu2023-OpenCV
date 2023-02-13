import cv2 as cv

# Membaca Gambar
img = cv.imread("Mochammad Gery Tauristino_5024221048_TugasOpenCV/Tugas1/tugas1.jpg")
img_resize = cv.resize(img, (600, 800))
img_copy = img_resize.copy()

# Memberikan warna pada posisi tertentu
cv.rectangle(img_resize, (0,0),(300,400), (0,0,255), cv.FILLED)
cv.rectangle(img_resize, (300,0),(600,400), (0,255,255), cv.FILLED)
cv.rectangle(img_resize, (300,400),(600,800), (0,255,0), cv.FILLED)
cv.rectangle(img_resize, (0,400),(300,800), (255,0,0), cv.FILLED)

# Blending warna dengan gambar
img_hasil = cv.addWeighted(img_resize, 0.5, img_copy, 0.5, 20)

# Menampilkan Gambar
cv.imshow("Hasil", img_hasil)
cv.imwrite("tugas1_done.jpg", img_hasil)

cv.waitKey(0)
cv.destroyAllWindows()
