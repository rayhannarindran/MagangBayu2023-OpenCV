import cv2 as cv
import numpy as np
import cvzone

#reading image, resizing, and generate the blank
img = cv.imread("tugas1.jpg")
img = cv.resize(img, (282,int(1003/2)))
blank = np.zeros(img.shape[:2], dtype='uint8')

#splitting color bgr
blue, green, red = cv.split (img)

#merging/insert splitted color to picture
c_cyan = cv.merge([blue, green, blank])
c_yellow = cv.merge([blank, green, red])
c_magenta = cv.merge([blue, blank, red])
c_green = cv.merge ([blank, green, blank])

#dividing picture into 4 pieces with different colour base
a = c_cyan [0:int(1003/4), 0:141]
b = c_yellow [0:int(1003/4), 141:282]
c = c_magenta [int(1003/4):1003, 0:141]
d = c_green [int(1003/4):1003, 141:282]

#dividing picture into 2 pieces with different colour base
e = c_cyan [:, 0:141]
f = c_yellow [:, 141:282]

#stacking divided picture
pict_4 = cvzone.stackImages([a,b, c, d], 2,1)
pict_2 = cvzone.stackImages([e,f], 2,1)

# make the result as a .jpg file
cv.imwrite("tugas1_done.jpg",pict_4)
# cv.imwrite("2 COLORS.jpg",pict_2)

#showing result
cv.imshow("GAMBAR ASLI", img)
cv.imshow("4 COLORS", pict_4)
cv.imshow("2 COLORS", pict_2)
cv.waitKey(0)
cv.destroyAllWindows()