import cv2 as cv
import numpy as np

img = cv.imread("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas3/tugas3.jpg")
# convert to hsv
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# range blue
low_bound = np.array([105,55,0])
up_bound = np.array([140,255,255])

# masking blue color
blue = cv.inRange(img_hsv, low_bound, up_bound) 
masked = cv.bitwise_and(img,img, mask=blue)

# get contours dari warna biru
contours, hierarchies = cv.findContours(blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(str(len(contours)))
# menggambar kontur
cv.drawContours(img, contours, 2, (0,0,0), 7)

peri = cv.arcLength(contours[2],True)
approx = cv.approxPolyDP(contours[2], 0.02*peri, True)
# print(approx) 
# #ini akan memberi kita point of corner point
print(f"{len(approx)}")
cv.putText(img,f"{len(approx)}",(100,150), cv.FONT_HERSHEY_DUPLEX,3,[0,0,0],5)

# cv.imshow("haha", masked) #buat ngecek dah bener atau belum masknya
cv.imshow("image", img)
# save image
cv.imwrite("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas3/tugas3_done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()