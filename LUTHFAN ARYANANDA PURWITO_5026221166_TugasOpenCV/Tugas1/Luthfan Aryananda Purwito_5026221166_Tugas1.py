# TASK 1
# Name  : Luthfan Aryananda Purwito
# ID    : 5026221166

# Importing libraries
import cv2 as cv
import numpy as np

# Read, Resize, and Copy the Image
img = cv.imread("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas1/tugas1.JPG")
imgResize = cv.resize(img, (500, 665))
imgNew = imgResize.copy()

# Making the Rectangles
# Row 1
cv.rectangle(imgNew, (0,0), (125,133), (255,0,0), -1) # BLUE (Row 1, Line 1)
cv.rectangle(imgNew, (0,133), (125,266), (255,255,0), -1) # CYAN/AQUA (Row 1, Line 2)
cv.rectangle(imgNew, (0,266), (125,399), (0,255,255), -1) # YELLOW (Row 1, Line 3)
cv.rectangle(imgNew, (0,399), (125,532), (255,0,255), -1) # PINK (Row 1, Line 4)
cv.rectangle(imgNew, (0,532), (125,665), (255,0,0), -1) # BLUE (Row 1, Line 5)
# Row 2
cv.rectangle(imgNew, (125,0), (250,133), (0,255,0), -1) # GREEN (Row 2, Line 1)
cv.rectangle(imgNew, (125,133), (250,266), (0,0,128), -1) # MAROON (Row 2, Line 2)
cv.rectangle(imgNew, (125,266), (250,399), (255,0,0), -1) # BLUE (Row 2, Line 3)
cv.rectangle(imgNew, (125,399), (250,532), (255,255,255), -1) # WHITE (Row 2, Line 4)
cv.rectangle(imgNew, (125,532), (250,665), (0,0,128), -1) # MAROON (Row 2, Line 5)
# Row 3
cv.rectangle(imgNew, (250,0), (375,133), (0,0,255), -1) # RED (Row 3, Line 1)
cv.rectangle(imgNew, (250,133), (375,266), (255,0,255), -1) # PINK (Row 3, Line 2)
cv.rectangle(imgNew, (250,266), (375,399), (0,255,255), -1) # YELLOW (Row 3, Line 3)
cv.rectangle(imgNew, (250,399), (375,532), (255,255,0), -1) # CYAN/AQUA (Row 3, Line 4)
cv.rectangle(imgNew, (250,532), (375,665), (0,255,255), -1) # YELLOW (Row 3, Line 5)
# Row 4
cv.rectangle(imgNew, (375,0), (500,133), (255,255,0), -1) # CYAN/AQUA (Row 4, Line 1)
cv.rectangle(imgNew, (375,133), (500,266), (128,0,0), -1) # NAVY BLUE (Row 4, Line 2)
cv.rectangle(imgNew, (375,266), (500,399), (0,255,0), -1) # GREEN (Row 4, Line 3)
cv.rectangle(imgNew, (375,399), (500,532), (0,0,255), -1) # RED (Row 4, Line 4)
cv.rectangle(imgNew, (375,532), (500,665), (255,0,255), -1) # PINK (Row 4, Line 5)

# Weighted Transparency
alpha = 0.3 # to set transparency level
res = cv.addWeighted(imgNew, alpha, imgResize, 1 - alpha, 0)

# Saving Image
cv.imwrite("Luthfan Aryananda Purwito_5026221166_TugasOpenCV/Tugas1/tugas1_done.jpg", res)

# Showing Images
cv.imshow("Filtered Picture", res)
cv.imshow("Original Picture", imgResize)

# Open until any key is pressed 
cv.waitKey(0)
cv.destroyAllWindows()