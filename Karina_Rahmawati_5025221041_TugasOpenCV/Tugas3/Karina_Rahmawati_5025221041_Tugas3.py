import cv2 as cv
import numpy as np

img = cv.imread("tugas3.jpg") #membaca gambar
img = cv.resize(img, (1200, 675)) #resize gambar

#convert BGR ke GRAY
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#membuat gambar biner
ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)

#mencari contour
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#menghitung sisi pada huruf H
cnt = contours[3]
epsilon = 0.01*cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
borders = len(approx)

#menulis jumlah sisi pada huruf H
cv.putText(img, str(borders), (10, 90), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)

#menggambar contour
cv.drawContours(img, [cnt], 0, (0, 0, 255), 4)

#menyimpan gambar
filename = "tugas3_done.jpg"
cv.imwrite(filename, img)

#menampilkan gambar
cv.imshow("Tugas 3", img)

cv.waitKey(0)
cv.destroyAllWindows()