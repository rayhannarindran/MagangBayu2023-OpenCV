import cv2 as cv
import numpy as np

# Read image
img = cv.imread("/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas1/tugas1.jpg")

# Get height and width
h, w = img.shape[:2]  #  save height, width

# Copy for base layer
output = img.copy()
# Make 4 square with different coordinate and color
cv.rectangle(img, (0, 0), (int(w/2), int(h/2)), (51, 51, 255), -1)
cv.rectangle(img, (int(w/2), 0), (int(w), int(h/2)), (119, 255, 51), -1)
cv.rectangle(img, (0, int(h/2)), (int(w/2), int(h)), (255, 229, 51), -1)
cv.rectangle(img, (int(w/2), int(h/2)), (int(w), int(h)), (51, 255, 242), -1)
# Make the image a certain dominant color
cv.addWeighted(img, 0.5, output, 0.5, 1, output)

# Print image
cv.imshow('red-green', output)
# Save image
cv.imwrite('/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas1/tugas1_done.jpg', output)

# Exiting the window if 'q' is pressed on the keyboard.
if cv.waitKey(0) & 0xFF == ord('q'): 
    cv.destroyAllWindows()