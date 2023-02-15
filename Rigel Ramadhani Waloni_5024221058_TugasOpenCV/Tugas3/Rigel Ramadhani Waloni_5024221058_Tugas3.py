# Import the Required Libraries
import cv2 as cv

# Read the Image
img = cv.imread("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas3/tugas3.jpg")

# Blur the Image
img_BLURRED = cv.GaussianBlur(img, (5,5), 0)

# Find Canny Edges
canny = cv.Canny(img_BLURRED, 125, 175)

# Find Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Draw the Contours
cv.drawContours(img, contours, 2, (0, 255, 0), 5)

# Count the Edges of the Contours
peri = cv.arcLength(contours[2], True)
simple_contour = cv.approxPolyDP(contours[2], 0.02 * peri, True)
num_sides = simple_contour.shape[0]

# Display text of number of sides
cv.putText(img, f"{num_sides}", (20, 70), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

# Display the Final Image
cv.imshow("FINAL | CONTOURS WITH NUMBER OF SIDES", img)

# Create the Final Image File (if needed)
cv.imwrite("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas3/tugas3_done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()