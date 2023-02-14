# TASK 2
# Name  : Luthfan Aryananda Purwito
# ID    : 5026221166

# Importing libraries
import cv2 as cv
import numpy as np

# Import, Resize, and Copy Image
img = cv.imread("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas2/tugas2.jpg")
res = img.copy()

# Pink Masking
# Converting to HSV
hsv = cv.cvtColor(res, cv.COLOR_BGR2HSV)
# Defining lower & upper limits
lower_pink = np.array([130, 50, 200])
upper_pink = np.array([170, 200, 255])
# Masking the image
mask = cv.inRange(hsv, lower_pink, upper_pink)
masked = cv.bitwise_and(res, res, mask=mask)

# Canny
canny = cv.Canny(masked, 125, 175)
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(res, contours, -1, (0,0,0), 2)

# Gray the image
gray = cv.cvtColor(masked, cv.COLOR_BGR2GRAY)

# Using moments to get the shape center
moment = cv.moments(gray)
x = int(moment["m10"] / moment["m00"])
y = int(moment["m01"] / moment["m00"])
cv.circle(res, (x,y), 5, (0,0,255), 1) # Circle the shape center

# Showing coordinates with cv.putText()
cv.putText(res, (f"center, x:{x}, y:{y}"), (x-60,y-20), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0))

# Saving image
cv.imwrite("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas2/tugas2_done.jpg", res)

# Showing images
cv.imshow("Original Image", img) # Showing Original Image
cv.imshow("Result", res) # Showing result

# Open until any key is pressed
cv.waitKey(0)
cv.destroyAllWindows()