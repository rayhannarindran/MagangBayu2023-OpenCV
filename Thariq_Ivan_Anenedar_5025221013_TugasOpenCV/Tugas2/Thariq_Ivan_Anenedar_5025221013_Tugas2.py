import cv2 as cv
import numpy as np

# Read image
img = cv.imread("/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas2/tugas2.jpg")
# Copy image for base
hasil = img
# Blurring image
img = cv.GaussianBlur(img, (5, 5), 0)
# Convert to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define range of blue color in HSV
lower_blue = np.array([140, 125, 50])
upper_blue = np.array([170, 255, 255])

# Threshold the HSV image to get only blue colors
mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask=mask_blue)
  
# Applying the Canny Edge filter
edge = cv.Canny(res, 50, 150)
  

# Find contours and hierarchy
contours, hierarchy = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  
# Going through every contours found in the image.
for cnt in contours :
    # Check if contour is edge or not
    approx = cv.approxPolyDP(cnt, 0.009 * cv.arcLength(cnt, True), True)
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
# Define i for loop
i = 0
# Assign first and last coordinate
x_awal, y_awal = n[0], n[1]
x_akhir, y_akhir = 0, 0

# Get coordinate of lowest and highest contour that found
for j in n :
    # Checking every coodinate and check for lowest and highest contour
    if(i % 2 == 0):
        x = n[i]
        y = n[i + 1]
        if(x < x_awal):
            if (x_awal > x_akhir):
                x_akhir = x_awal
            x_awal = x
        else:
            if (x > x_akhir):
                x_akhir = x

        if(y < y_awal):
            if (y_awal > y_akhir):
                y_akhir = y_awal
            y_awal = y
        else:
            if (y > y_akhir):
                y_akhir = y
    i += 1
# Calculate center point
x_coor = (x_akhir+x_awal)/2
y_coor = (y_akhir+y_awal)/2
# Creates the string to be printed
string = 'center, x: '+ str(int(x_coor)) + ' , y: ' + str(int(y_coor))  
# Print string above center point
cv.putText(hasil, string, (1035, 435),cv.FONT_ITALIC, 0.5, (0, 0, 0), 1) 
# Add circle at center point
hasil = cv.circle(hasil, (int(x_coor),int(y_coor)), radius=0, color=(0, 0, 255), thickness=3)
# Draws boundary of contours.
cv.drawContours(hasil, contours, -1, (255, 0, 0), 3)
# Showing the final image.
cv.imshow('image3', hasil) 
# Save final image
cv.imwrite('/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas2/tugas2_done.jpg', hasil)
  
# Exiting the window if 'q' is pressed on the keyboard.
if cv.waitKey(0) & 0xFF == ord('q'): 
    cv.destroyAllWindows()