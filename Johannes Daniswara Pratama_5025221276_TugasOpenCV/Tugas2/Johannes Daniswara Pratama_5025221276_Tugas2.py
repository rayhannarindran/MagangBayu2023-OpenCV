import cv2 as cv
import numpy as np

# Johannes Daniswara Pratama - 5025221276

# Load the image
img = cv.imread("Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas2/tugas2.jpg")

# Convert to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Apply median blur . I tested gaussian blur and median blur, and the result is better on median blur
blured = cv.medianBlur(hsv, 5)

# Define the range of pink color in HSV color space
lower_pink = np.array([146, 100, 50])
upper_pink = np.array([162, 255, 255])

# Threshold range to generate mask
mask_pink = cv.inRange(blured, lower_pink, upper_pink)

# Find contours in the mask
contours, hierarchy = cv.findContours(mask_pink, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Loop through each contour 
for i in contours:
    # Calculate the moments of the contour (for knowing center point)
    # More info on cv.moments , check opencv documentation -> https://docs.opencv.org/3.4/d0/d49/tutorial_moments.html
    M = cv.moments(i)

    # Check if the moments of countour is not zero
    if M['m00'] !=0:

        # Calculate the center point of the contour
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        center_point = (cX, cY)

        # Draw the center point and put text
        cv.circle(img, center_point, 5, (0, 0, 255), -1)
        cv.putText(img, f"center, x:{cX}, y:{cY}", (cX-100, cY-20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        # Draw the contour on the image (blue)
        cv.drawContours(img, [i], 0, (255, 0, 0), 5)

# Save the image
cv.imwrite("Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas2/tugas2_done.jpg",img)
# Show the resulting image
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()
