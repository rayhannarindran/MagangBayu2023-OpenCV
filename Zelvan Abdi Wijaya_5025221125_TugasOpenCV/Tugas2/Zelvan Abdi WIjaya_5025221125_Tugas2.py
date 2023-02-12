import cv2 as cv
import numpy as np

img = cv.imread('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas2/tugas2.jpg')

# Convert BGR to HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# pink color range
lower = np.array([140,50,50])
upper = np.array([180,255,255])

# Threshold to get only pink colors
mask = cv.inRange(img_hsv, lower, upper)

# Find the contours of the frame
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw the contours with yellow color
countour_img = cv.drawContours(img, contours, -1, (0,255,255), 3)

for a in contours:
    # Find the center of the contour
    M = cv.moments(a)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

# circle in the center of the contour
cv.circle(countour_img, (cX, cY), 7, (0, 0, 255), -1)
#  Write the text in the center of the contour using black color
cv.putText(countour_img, "center, x: " +str(cX)+", y: "+str(cY), (cX - 100, cY - 20), cv.FONT_HERSHEY_SIMPLEX, 
            0.5, (0, 0,0), 2)          
cv.imshow("Result", countour_img)
cv.imwrite('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas2/tugas2_done.jpg', countour_img)
cv.waitKey(0)