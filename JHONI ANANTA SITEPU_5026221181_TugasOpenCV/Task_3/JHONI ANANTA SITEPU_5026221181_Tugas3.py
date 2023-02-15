import cv2 as cv
import numpy as np

# read the image 
img = cv.imread("C:\\Users\yoga\MagangBayu2023-OpenCV\JHONI ANANTA SITEPU_5026221181_TugasOpenCV\Task_3\GAMBAR_TUGAS3.jpg")

# Copy image for output 
output = img.copy()

# Rescale gambar
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Canny algorithms for finding the edge of the image
canny = cv.Canny(output, 100, 200)

# Search contour
contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

# Draw contour
cv.drawContours(output, contours, -1, (0,0,255), 2)

# Count each side the contours had
perimeter = cv.arcLength(contours[3], True)
approx = cv.approxPolyDP(contours[3], 0.02 * perimeter, True)

# Put text on left edge of image
cv.putText(output, str(len(approx)), (20, 70), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)

# Showing Images
cv.imshow("Original image", rescaleFrame(img))
cv.imshow("Result", rescaleFrame(output))

# Saving Image
cv.imwrite("tugas3_done.jpg", output)

cv.waitKey(0)
cv.destroyAllWindows()