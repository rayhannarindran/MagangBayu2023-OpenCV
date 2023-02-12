import cv2 as cv
import numpy as np

img = cv.imread('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas3/tugas3.jpg')

# Convert BGR to HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# blue color range
lower = np.array([90,50,50])
upper = np.array([150,255,255])

# Threshold to get only blue colors
mask = cv.inRange(img_hsv, lower, upper)

# Find the contours of the frame
contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# Initialize the list of inner contours
countours = []

# in order to get the inner contours, we need to check the hierarchy
for i, countour in enumerate(contours):
    if(hierarchy[0][i][3] == 1):
        countours.append(countour)

# draw all inner contours using red color
countour_img = cv.drawContours(img, countours, -1, (0,0,255), 5)

for i in countours:
    # count the number of sides of the inner contours
    sides = cv.approxPolyDP(i, 0.01*cv.arcLength(i, True), True)

cv.putText(countour_img, str(len(sides)),(20,100), cv.FONT_ITALIC, 3, (0,0,0), 2)
cv.imshow("Result", countour_img)
cv.imwrite('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas3/tugas3_done.jpg', countour_img)
cv.waitKey(0)