import cv2 as cv
import numpy as np

# Searching total edge 
def search_edge(img_search) -> int:
    # Resize and crop image
    img_search = cv.resize(img_search,(640,360))
    img_search = img_search[80:190, 260:360]
    
    # Convert to HSV
    hsv = cv.cvtColor(img_search, cv.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([10, 100, 120])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(img_search, img_search, mask=mask_blue)

    # Applying the Canny Edge filter
    edge = cv.Canny(res, 50, 150)

    # #find contours
    contours, hierarchy = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    
    # Going through every contours found in the image.
    for cnt in contours :
        # Check if contour is edge or not
        approx = cv.approxPolyDP(cnt, 0.009 * cv.arcLength(cnt, True), True)
        # Used to flatted the array containing
        # the co-ordinates of the vertices.
        n = approx.ravel() 
    
    # Return total edge contour found
    return str(int(len(n)/2))

# Read image
img = cv.imread("/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas3/tugas3.jpg")  
# Copy for base image
hasil = img
# Blurring image
img = cv.GaussianBlur(img, (5, 5), 0)


# Convert to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define range of blue color in HSV
lower_blue = np.array([100, 75, 10])
upper_blue = np.array([120, 255, 255])

# Threshold the HSV image to get only blue colors
mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask=mask_blue)

# Applying the Canny Edge filter
edge = cv.Canny(res, 50, 150)

# Find contours
contours, hierarchy = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# Print text
cv.putText(hasil, search_edge(img), (25, 100),cv.FONT_ITALIC, 3, (0, 0, 0),3) 
# Draw contours
cv.drawContours(hasil, contours, 0, (0, 0, 255), 2)
# Show result
cv.imshow("Hasil", hasil)
# Save result
cv.imwrite('/home/ivan/magang-opencv/MagangBayu2023-OpenCV/Thariq_Ivan_Anenedar_5025221013_TugasOpenCV/Tugas3/tugas3_done.jpg', hasil)

# Exiting the window if 'q' is pressed on the keyboard.
if cv.waitKey(0) & 0xFF == ord('q'): 
    cv.destroyAllWindows()