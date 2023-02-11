import cv2 as cv
import numpy as np

# Load and resize image
img = cv.imread('tugas1.jpg')
img = cv.resize(img, (640, 360))

# Divide the image into 4 equal parts
height, width = img.shape[:2]
# Split into vertical part
split1, split2, = np.vsplit(img, 2)

# Split again into horizontal part
part1, part2 = np.hsplit(split1, 2)
part3, part4 = np.hsplit(split2, 2)

# Create a green color mask
mask1 = np.full(part1.shape, (0, 255, 0), dtype=np.uint8) # Green color

# Create a red color mask
mask2 = np.full(part1.shape, (0, 0, 255), dtype=np.uint8)# Red color

# Create a yellow color mask
mask3 = np.full(part1.shape, (0, 255, 255), dtype=np.uint8) # Yellow color

# Create a blue color mask
mask4 = np.full(part1.shape, (255, 0, 0), dtype=np.uint8) # Blue color

# Apply the green mask to all part with thickness of 0.7
# More info on cv.addWeighted : https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html  -> opencv documentation
result1 = cv.addWeighted(part1, 1, mask1, 0.7, 0)
result2 = cv.addWeighted(part2, 1, mask2, 0.7, 0)
result3 = cv.addWeighted(part3, 1, mask3, 0.7, 0)
result4 = cv.addWeighted(part4, 1, mask4, 0.7, 0)

# Combine the results back into a single image
result = np.concatenate((np.concatenate((result1, result2), axis=1), np.concatenate((result3, result4), axis=1)), axis=0)

# Show the resulting image
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()