import cv2 as cv
import numpy as np

# Read image
img = cv.imread("C:\\Users\yoga\MagangBayu2023-OpenCV\JHONI ANANTA SITEPU_5026221181_TugasOpenCV\Task_2\GAMBAR_TUGAS2.jpg")

# Rescale gambar
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# copy img
output = img.copy()

# Convert src to hsv colorspace
img_hsv= cv.cvtColor(output, cv.COLOR_BGR2HSV)

# Upper and lower limits to color detection
lower = np.array([140, 50, 200])
upper = np.array([170, 200, 255])

# Detect the square color
img_mask = cv.inRange(img_hsv, lower, upper)
img_masked= cv.bitwise_and(output, output, mask=img_mask)

# Canny Edges
canny = cv.Canny(img_masked, 30, 200)

# The mask contour
countours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw the countours
cv.drawContours(output, countours, -1, (255,0,0), 2)

# Gray image
gray = cv.cvtColor(img_masked, cv.COLOR_BGR2GRAY)

# Find the moments
moment = cv.moments(gray)
x = int(moment['m10'] / moment['m00'])
y = int(moment['m01'] / moment['m00'])

# Draw circle and put text in the middle
cv.circle(output, (x,y), 5, (255, 0, 0), 1)
cv.putText(output, (f"center, x:{x}, y:{y}"), (x-60, y-20), cv.FONT_HERSHEY_PLAIN, 0.8, (0,0,0) )

cv.imshow("Original", rescaleFrame(img))
cv.imshow("result", rescaleFrame(output)) 

# Write the result
cv.imwrite("tugas2_done.jpg", output)

cv.waitKey(0)
cv.destroyAllWindows()