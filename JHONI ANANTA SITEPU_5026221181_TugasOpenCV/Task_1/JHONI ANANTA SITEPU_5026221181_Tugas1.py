import cv2 as cv
import numpy as np

# Rescale gambar
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# load image
img = cv.imread('C:\\Users\yoga\MagangBayu2023-OpenCV\JHONI ANANTA SITEPU_5026221181_TugasOpenCV\Task_1\Car.jpg')
# Show the original image
cv.imshow("Car Original", rescaleFrame(img))
# Mendapatkan tinggi dan lebar gambar
height, width= (img.shape[0], img.shape[1])

# Copy for base layer
output = img.copy()

# Make 2 square spliting verticaly and different color
cv.rectangle(img, (0,0), (int(width/2), int(height)), (51, 51, 255), -1)
cv.rectangle(img, (int(width/2), 0), (int(width), int(height)), (255, 0, 0), -1)

cv.addWeighted(img, 0.5, output, 0.5, 1, output)

cv.imshow("Car New", rescaleFrame(output))

# Write the red-blue car
cv.imwrite("tugas1_done.jpg", output)

cv.waitKey(0)
cv.destroyAllWindows()