# Import the Required Libraries
import cv2 as cv

# Read the Image
img = cv.imread("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas2/tugas2.jpg")

# Blur Image
img_BLURRED = cv.GaussianBlur(img, (5,5), 0)

# Find Canny Edges
canny = cv.Canny(img_BLURRED, 30, 200)

# Find Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Find the Center of Contour
for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.drawContours(img, contours, 2, (255, 0, 0), 5)
        cv.circle(img, (cx, cy), 7, (255, 0, 0), -1)
        cv.putText(img, f"Center, x:{cx}, y:{cy}", (cx - 90, cy - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

# Display the Final Image with Center Point and Contours
cv.imshow("TASK 2 | CONTOURS IMAGE WITH CIRCLE IN THE MIDDLE OF THE CONTOURS", img)

# Create the Final Image File (if needed)
cv.imwrite("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas2/tugas2_done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()