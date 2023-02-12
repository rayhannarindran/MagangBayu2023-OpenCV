import cv2 as cv
import numpy as np

# Johannes Daniswara Pratama - 5025221276

# Load and resize image
img = cv.imread("Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas1/tugas1.jpg")

# create height and width variable from img.shape
height, width = img.shape[:2]

# Split into 4 equal parts 
part1 = img[:int(height/2), :int(width/2)]
part2 = img[:int(height/2), int(width/2):width]
part3 = img[int(height/2):height, :int(width/2)]
part4 = img[int(height/2):height, int(width/2):width]

# Create a green, red, yellow, and blue color mask
mask1 = np.full(part1.shape, (0, 255, 0), dtype=np.uint8) # Green color
mask2 = np.full(part2.shape, (0, 0, 255), dtype=np.uint8)# Red color
mask3 = np.full(part3.shape, (0, 255, 255), dtype=np.uint8) # Yellow color
mask4 = np.full(part4.shape, (255, 0, 0), dtype=np.uint8) # Blue color

# Apply the green, red , yellow , and blue mask to corresponding part with thickness of 0.7
# More info on cv.addWeighted : https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html  -> opencv documentation
result1 = cv.addWeighted(part1, 1, mask1, 0.7, 0)
result2 = cv.addWeighted(part2, 1, mask2, 0.7, 0)
result3 = cv.addWeighted(part3, 1, mask3, 0.7, 0)
result4 = cv.addWeighted(part4, 1, mask4, 0.7, 0)

# Combine the results back into a single image
result = np.concatenate((np.concatenate((result1, result2), axis=1), np.concatenate((result3, result4), axis=1)), axis=0)

# Save the images
cv.imwrite("Johannes Daniswara Pratama_5025221276_TugasOpenCV/Tugas1/tugas1_done.jpg",result)
# Show the resulting image
cv.imshow('shape', result)
cv.waitKey(0)
cv.destroyAllWindows()