import cv2
import numpy as np

import os
os.chdir("Tugas1")

# read img
img = cv2.imread('tugas1.jpg')

# get areas
height, width = img.shape[:2]

# partition
part_1 = img[0:height//2, 0:width//2]
part_2 = img[0:height//2, width//2:width]
part_3 = img[height//2:height, 0:width//2]
part_4 = img[height//2:height, width//2:width]

# convert to green
part_1= cv2.cvtColor(part_1, cv2.COLOR_BGR2HSV)
part_1[:, :, 0] = 60
part_1= cv2.cvtColor(part_1, cv2.COLOR_HSV2BGR)

# red
part_2= cv2.cvtColor(part_2, cv2.COLOR_BGR2HSV)
part_2[:, :, 0] = 0
part_2= cv2.cvtColor(part_2, cv2.COLOR_HSV2BGR)

# blue
part_3= cv2.cvtColor(part_3, cv2.COLOR_BGR2HSV)
part_3[:, :, 0] = 120
part_3= cv2.cvtColor(part_3, cv2.COLOR_HSV2BGR)

# yellow
part_4= cv2.cvtColor(part_4, cv2.COLOR_BGR2HSV)
part_4[:, :, 0] = 30
part_4= cv2.cvtColor(part_4, cv2.COLOR_HSV2BGR)

# Make a frame
merged_image = np.zeros((height, width, 3), np.uint8)

# get area of partition
height, width, _ = part_1.shape

# organize partition
merged_image[:height, :width, :] = part_1
merged_image[:height, width:, :] = part_2
merged_image[height:, :width, :] = part_3
merged_image[height:, width:, :] = part_4

cv2.imwrite('tugas1_done.jpg', merged_image)
cv2.imshow('tugas1_done.jpg', merged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()