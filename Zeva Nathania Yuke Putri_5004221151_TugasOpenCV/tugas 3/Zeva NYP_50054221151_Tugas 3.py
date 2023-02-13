import cv2 as cv
import numpy as np
import imutils as imt

## read image
img = cv.imread("gtt.jpg")
## resize image
img = cv.resize(img, (1366, 768))

## threshold, gray && blurred
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5,5), 0)
thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)[1]

## to figure 'H' contour
contours3, hierarchy1 = cv.findContours(thresh.copy(), cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
img_copy3 = img.copy()
cv.drawContours(img_copy3, contours3, 1, (0,255,0), 2, cv.LINE_AA)

x, y, w, h = 0, 0, 400, 250

## add text 12 on left corner 
cv.putText(img=img_copy3, text="12", org=(x + int(w/10),y + int(h/1.5)), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=4, color=(255,0,0), thickness=7)

## show && save
cv.imshow("gtt", img_copy3)
cv.imwrite("Tugas3.jpg", img_copy3)
cv.waitKey(0)
cv.destroyAllWindows()