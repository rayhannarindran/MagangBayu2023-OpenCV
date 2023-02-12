import cv2
import numpy as np

import os
os.chdir("Tugas3")

# read img
img = cv2.imread('tugas3.jpg')

# resize img
h, w, c = img.shape
img = cv2.resize(img, (int(w/2), int(h/2)))

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting edges
edges = cv2.Canny(gray, 170, 255)

# take areas with more intensity
ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

# get all contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for each contour
for contour in contours:
    # get length from each contour
    peri = cv2.arcLength(contour, True)
    # get dots
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

# draw contour
cv2.drawContours(img, [contour], -1, (0,0,255), 2)

# add label
img = cv2.putText(img, '{}'.format(len(approx)), (0,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 1, cv2.LINE_AA)

cv2.imshow('tugas3_done', img)
cv2.imwrite('tugas3_done.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()