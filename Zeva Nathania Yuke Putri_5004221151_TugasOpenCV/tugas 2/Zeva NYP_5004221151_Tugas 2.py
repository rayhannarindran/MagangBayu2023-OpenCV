import cv2 as cv 
import numpy as np
import imutils as imt
# import matplotlib.figure as plt 

img = cv.imread("out.png")

## image has alrd being resized as follow
# img = cv.resize(img, (1366, 768))

## extract color onto hsv ((since my bad been using GRAY instead, for multiple times ://))
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

## set up a range in order to mask
lower_img = np.array([120,0,0])
upper_img = np.array([170,255,255])

## mask time!!
masking = cv.inRange(img_hsv, lower_img, upper_img)
ret_img = cv.bitwise_and(img,img,mask=masking)

## not least to do threshold
## started by gray-ing and blurring
img_gray = cv.cvtColor(ret_img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(img_gray, (5, 5), 0)
thresh = cv.threshold(blurred, 110, 255, cv.THRESH_BINARY)[1]

## blushing contour!
contours = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours = imt.grab_contours(contours)

# cv.imshow("out_image", img)

for ct in contours:
    # found the center
    M = cv.moments(ct)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
    # center = (cx, cy) 
cv.drawContours(img, [ct], -1, (0, 0, 0), 2)
cv.circle(img, (cx, cy), 5, (0, 0, 255), -1)
    
    # put text
cntext = "center, x: " + str(cx) + ". y: " + str(cy)
cv.putText(img, cntext, (cx - 77, cy - 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 0, 0), 3)

cv.imwrite("Tugas2.png", img)
cv.imshow("tata", img)
cv.imshow("tata", cntext)
cv.waitKey(0)
cv.destroyAllWindows()
