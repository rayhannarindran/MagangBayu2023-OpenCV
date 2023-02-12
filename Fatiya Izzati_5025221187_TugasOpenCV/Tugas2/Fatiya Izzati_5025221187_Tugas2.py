import cv2 as cv
import numpy as np
import imutils as mul

#reading image, resizing
img = cv.imread("tugas2.jpg")
img = cv.resize(img, (800,450))

#change to hsv color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#make range lower and upper to do masking
lower=np.array([120, 0, 0])
upper=np.array([170, 255, 255])

#masking
mask_mag=cv.inRange(hsv,lower,upper)
res = cv.bitwise_and(img,img,mask=mask_mag)

#change to gray color, blurring, and threshold to do countour
gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
thresh = cv.threshold(blurred, 100, 255, cv.THRESH_BINARY)[1]

#find contour
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = mul.grab_contours(cnts)

cv.imshow ("GAMBAR ASLI", img)

for c in cnts:
    # compute the center of the contour
    M = cv.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    cv.drawContours(img, [c], -1, (0, 0, 0), 2)
    cv.circle(img, (cX, cY), 5, (0, 0, 255), -1)
    #putting text
    textField = "center, x: " + str(cX) + ", y: " + str(cY)
    cv.putText(img, textField, (cX - 85, cY - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

#make the result as a .jpg file and show
cv.imwrite("tugas2_done.jpg",img)
cv.imshow("RESULT", img)

cv.waitKey(0)
cv.destroyAllWindows()