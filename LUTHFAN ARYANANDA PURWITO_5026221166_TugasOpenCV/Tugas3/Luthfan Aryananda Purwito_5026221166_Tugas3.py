# TASK 3
# Name  : Luthfan Aryananda Purwito
# ID    : 5026221166

# Importing libraries
import cv2 as cv
import numpy as np

# Import, Resize, and Copy Image
img = cv.imread("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas3/tugas3.jpg")
res = img.copy()

# Blue Masking
# Converting to HSVs
hsv = cv.cvtColor(res, cv.COLOR_BGR2HSV)
# Defining lower & upper limits
lower_blue = np.array([85, 50, 50])
upper_blue = np.array([140, 255, 255])
# Masking the image
mask = cv.inRange(hsv, lower_blue, upper_blue)
masked = cv.bitwise_and(res, res, mask=mask)

# Canny Algorithm (to find edges)
canny = cv.Canny(masked, 125, 175)
contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(res, contours, 3, (0,0,0), 6)

# Counting the number of vertices
outline = cv.arcLength(contours[3], True)
approx = cv.approxPolyDP(contours[3], 0.02 * outline, True)
cv.putText(res, str(len(approx)), (20, 70), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)

# Showing Images
cv.imshow("Original Image", img) # Showing Original Image
cv.imshow("Result", res) # Showing result

# Saving Image
cv.imwrite("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas3/tugas3_done.jpg", res)

# Open until any key is pressed
cv.waitKey(0)
cv.destroyAllWindows()