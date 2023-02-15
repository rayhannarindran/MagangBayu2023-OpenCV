# Import the Required Libraries
import cv2 as cv
import numpy as np

# Read the Image
img = cv.imread("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas2/tugas2.jpg")

# Convert the Color Space Image to HSV
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# For Detecting/Masking Pink Color
lower_bounds = np.array([145, 100, 50]) # The lower of Color Range
upper_bounds = np.array([165, 255, 255]) # The upper of Color Range
masking = cv.inRange(img_HSV, lower_bounds, upper_bounds) # Masking Pink Color Only

# Find Canny Edges
canny = cv.Canny(masking, 30, 200)

# Find Contours
contours, hierarchies = cv.findContours(masking, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Find the Center of Contour
for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

# Draw the Contours
cv.drawContours(img, [i], -1, (255, 0, 0), 5)

# Create Circle in the Center of Contour
cv.circle(img, (cx, cy), 7, (0, 0, 255), -1)

# Put Text Above the Circle
cv.putText(img, f"Center, x:{cx}, y:{cy}", (cx - 90, cy - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

# Display the Final Image with Center Point and Contours
cv.imshow("TASK 2 | CONTOURS IMAGE WITH CIRCLE IN THE MIDDLE OF THE CONTOURS", img)

# Create the Final Image File
cv.imwrite("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas2/tugas2_done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()