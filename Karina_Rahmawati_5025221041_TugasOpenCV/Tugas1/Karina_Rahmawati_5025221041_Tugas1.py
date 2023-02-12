import cv2 as cv
import numpy as np
import cvzone

img = cv.imread("tugas1.jpg") #membaca gambar
img = cv.resize(img, (684, 456)) #resize gambar

#convert BGR ke HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#split HSV channel
h, s, v = cv.split(img_hsv)
h.fill(0)
s.fill(255)

#merubah value warna menjadi dominan merah
h1 = np.mod(h, 180).astype(np.uint8)
top1 = cv.merge([h1, s, v])

#merubah value warna menjadi dominan orange
h2 = np.mod(h + 20, 180).astype(np.uint8)
top2 = cv.merge([h2, s, v])

#merubah value warna menjadi dominan kuning
h3 = np.mod(h + 30, 180).astype(np.uint8)
top3 = cv.merge([h3, s, v])

#merubah value warna menjadi dominan hijau
h4 = np.mod(h + 55, 180).astype(np.uint8)
top4 = cv.merge([h4, s, v])

#merubah value warna menjadi dominan biru muda
h5 = np.mod(h + 90, 180).astype(np.uint8)
bottom1 = cv.merge([h5, s, v])

#merubah value warna menjadi dominan biru tua
h6 = np.mod(h + 120, 180).astype(np.uint8)
bottom2 = cv.merge([h6, s, v])

#merubah value warna menjadi dominan ungu
h7 = np.mod(h + 135, 180).astype(np.uint8)
bottom3 = cv.merge([h7, s, v])

#merubah value warna menjadi dominan pink
h8 = np.mod(h + 150, 180).astype(np.uint8)
bottom4 = cv.merge([h8, s, v])

#memotong gambar
h, w = img_hsv.shape[:2]
X1, X2, X3, Y1 = (w // 4), (w // 2), (3 * w // 4), (h // 2)

top1 = top1[0:Y1, 0:X1]
top2 = top2[0:Y1, X1:X2]
top3 = top3[0:Y1, X2:X3]
top4 = top4[0:Y1, X3:w]
bottom1 = bottom1[Y1:h, 0:X1]
bottom2 = bottom2[Y1:h, X1:X2]
bottom3 = bottom3[Y1:h, X2:X3]
bottom4 = bottom4[Y1:h, X3:w]

#menggabungkan semua partisi/potongan gambar
imagestack = cvzone.stackImages([top1, top2, top3, top4, bottom1, bottom2,bottom3, bottom4], 4, 1)

#convert HSV ke BGR
img_new = cv.cvtColor(imagestack, cv.COLOR_HSV2BGR)

#menyimpan gambar
filename = "tugas1_done.jpg"
cv.imwrite(filename, img_new)

#menampilkan gambar
cv.imshow("Tugas 1", img_new)

cv.waitKey(0)
cv.destroyAllWindows()