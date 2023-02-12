import cv2 as cv
import numpy as np

# Johannes Daniswara Pratama

# Load the image
img = cv.imread('Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas3/tugas3.jpg')
  
# converting image into HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold range to generate mask
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Find contours in the mask
contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  
# list for storing names of shapes
for i in contours:

    # cv.approxPloyDP() function to approximate the shape and count the corner . More info on opencv documentation
    corner = cv.approxPolyDP( i, 0.01 * cv.arcLength(i, True), True)

    # If length of corner is 12 , then it will draw the countour 
    if len(corner) == 12:
        # Draw countour with green colour
        cv.drawContours(img, [i], 0, (0,255,0), 6)
        # Put the text "Amount of corner"
        cv.putText(img, f"{len(corner)}", (40,100), cv.FONT_HERSHEY_DUPLEX, 3, (0, 0, 0), 3)


# Save the image
cv.imwrite("Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas3/tugas3_done.jpg",img)
# displaying the image after drawing contours
cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()