import cv2 as cv
import numpy as np

img = cv.imread("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas2/tugas2.jpg")
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# menfilter warna pink
low_bound = np.array([115,60,190])
up_bound = np.array([170,160,255])
pink = cv.inRange(img_hsv, low_bound, up_bound) 
# masking only warna pink
masked = cv.bitwise_and(img,img, mask=pink)

# mencari contours dan hierarchies
contours, hierarchies = cv.findContours(pink, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# contur terluar yaitu contours[0] -> jadi hanya perlu draw contour[0]
cv.drawContours(img, contours, 0, (255,0,0), 7)

# mencari titik tengah dari suatu contour
cnt = contours[0]
M = cv.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# menggambar titik pada titik pusat
cv.circle(img,(cx,cy),7,[255,0,0],cv.FILLED)
print(f"x : {cx} dan y : {cy}")
# menuliskan teks pada titik pusat
cv.putText(img,f"centernya x : {cx} y : {cy}",(cx-130,cy-20), cv.FONT_HERSHEY_DUPLEX,0.6,[0,0,0],2)
# cv.imshow("haha", masked) #buat ngecek dah bener atau belum masknya
cv.imshow("image", img)
cv.imwrite("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas2/tugas2_done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()