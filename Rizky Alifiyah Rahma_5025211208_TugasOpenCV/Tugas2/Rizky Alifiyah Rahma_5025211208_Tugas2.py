import cv2
import numpy as np

import os
os.chdir("Tugas2")

# read img
img = cv2.imread('tugas2.jpg')

# resize img
h, w, c = img.shape
img = cv2.resize(img, (int(w/2), int(h/2)))

# blurred img
img_BLURRED = cv2.GaussianBlur(img, (5,5), 0)

# convert to hsv
hsv = cv2.cvtColor(img_BLURRED, cv2.COLOR_BGR2HSV)

# get lower and upper
lower_pink = np.array([145, 50, 50])
upper_pink = np.array([180, 255, 255])

# get a pink mask
mask = cv2.inRange(hsv, lower_pink, upper_pink)

# join img with mask
result = cv2.bitwise_and(img_BLURRED, img_BLURRED, mask=mask)

# detect edges
canny = cv2.Canny(result, 125, 175)

# find contour
contours, hierarchies = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# draw contour
cv2.drawContours(img, contours, -1, (0, 0, 0), 2)

# find a big contour
cnt = max(contours, key=cv2.contourArea)

# find center
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# Show center
print("Titik Tengah: ({}, {})".format(cX, cY))

# add label
img = cv2.putText(img, 'Center, x: {}, y: {}'.format(cX, cY), (cX-50, cY-7), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1, cv2.LINE_AA)

# add dot in center
img = cv2.circle(img, (cX, cY), 0, (0, 0, 255), 5)

cv2.imshow("tugas2_done.jpg", img)
cv2.imwrite("tugas2_done.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()