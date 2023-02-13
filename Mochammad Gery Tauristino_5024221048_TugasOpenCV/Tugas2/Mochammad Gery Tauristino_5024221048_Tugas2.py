import cv2 as cv
import numpy as np

# Membaca Gambarnya
image = cv.imread("Mochammad Gery Tauristino_5024221048_TugasOpenCV/Tugas2/tugas2.jpg")
img = image

# Menampilkan Gambar original
cv.imshow("TUGAS 2.1", image)

# Konversi ke HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Mencari warna pink pada gambar
lower_pink = np.array([150, 85, 50])
upper_pink = np.array([165, 255, 255])
mask = cv.inRange(hsv, lower_pink, upper_pink)

#Mencari contoursnya
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#Mencari Center dari Contour yang dipilih
for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.drawContours(img, [i], -1, (0, 0, 0), 3)
        cv.circle(img, (cx, cy), 7, (0, 0, 0), -1)
        cv.putText(img, "center", (cx - 20, cy - 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv.putText(img, "x :" + str(cx) + " y :" + str(cy), (cx - 35, cy - 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

#Menampilkan Gambar yang sudah diedit
cv.imshow("TUGAS 2", img)
cv.imwrite("tugas2_done.jpg",img)

cv.waitKey(0)
cv.destroyAllWindows()
