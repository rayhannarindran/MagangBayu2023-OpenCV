import cv2 as cv
import numpy as np

#membaca gambar
img = cv.imread("tugas2.jpg")

#convert BGR ke HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#masking warna pink
lower_bounds = np.array([150, 50, 50])
upper_bounds = np.array([170, 255, 255])
mask = cv.inRange(img_hsv, lower_bounds, upper_bounds)
img_masked = cv.bitwise_and(img, img, mask = mask)

#canny edge
canny = cv.Canny(img_masked, 50, 150)

#mencari contour
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#menggambar contour
cnt = contours[0]
cv.drawContours(img, [cnt], 0, (0, 0, 0), 4)

#mencari titik tengah kotak
M = cv.moments(cnt)
if M['m00'] != 0:
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    #mengammbar titik pada bagian tengah kotak
    cv.circle(img, (cx, cy), 5, (0, 0, 255), -1)

    #menulis posisi titik
    cv.putText(img, "center, x: " + str(cx) + ", y:" + str(cy), (cx - 80, cy - 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

#menyimpan gambar
filename = "tugas2_done.jpg"
cv.imwrite(filename, img)

#menapilkan gambar
cv.imshow("Tugas 2", img)

cv.waitKey(0)
cv.destroyAllWindows()