import cv2 as cv 
import numpy as np
import cvzone

## required image // raw
img = cv.imread("Valo.jpg")

## begin by dividing an image onto 4 sections 
## vertical divide image
## start!!!
height = img.shape[0]
width = img.shape[1]
## cut an image into a half 
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]
## finishing vertical divide image

## counter clockwising so it would turns to 4 sections 
## rotate image LEFT1 to 90 CLOCKWISE
img= cv.rotate(left1, cv.ROTATE_90_CLOCKWISE)

## starting vertical divide image
height = img.shape[0]
width = img.shape[1]

## cut off the image on a half 
width_cutoff = width // 2
l1 = img[:, :width_cutoff]
l2 = img[:, width_cutoff:]
## finish vertical divide image 
## rotate image to 90 counterclockwise
l1 = cv.rotate(l1, cv.ROTATE_90_COUNTERCLOCKWISE)
#save
# cv.imwrite("valo_1.jpg", l1)
#rotate image to 90 COUNTERCLOCKWISE
l2 = cv.rotate(l2, cv.ROTATE_90_COUNTERCLOCKWISE)
# #save
# cv.imwrite("valo_2.jpg", l2)

# ## horizontal divide right1 image
# ## rotate image RIGHT1 to 90 CLOCKWISE
img = cv.rotate(right1, cv.ROTATE_90_CLOCKWISE)
# ## start vertical divide image
height = img.shape[0]
width = img.shape[1]
# # Cut the image in half
width_cutoff = width // 2
r1 = img[:, :width_cutoff]
r2 = img[:, width_cutoff:]
# # finish vertical devide image
#rotate image to 90 COUNTERCLOCKWISE
r1 = cv.rotate(r1, cv.ROTATE_90_COUNTERCLOCKWISE)
# #save
# cv.imwrite("rant_1.jpg", r1)
# #rotate image to 90 COUNTERCLOCKWISE
r2 = cv.rotate(r2, cv.ROTATE_90_COUNTERCLOCKWISE)
# #save
# cv.imwrite("rant_2.jpg", r2)

img = cv.imread("rant_1.jpg")
img1 = cv.imread("rant_2.jpg")
img2 = cv.imread("valo_1.jpg")
img3 = cv.imread("valo_2.jpg")

# returns the array filled with zeros  of floating values by default 
zero = np.zeros(img1.shape[:2], dtype='uint8')
uno = np.zeros(img2.shape[:2], dtype='uint8')
tres = np.zeros(img3.shape[:2], dtype='uint8')

# # define img's color 
# # blue, green, red = cv.split(img)
# # extract color into plain since no need to extract 
# # zeroimg = cv.merge([blank, white, blank])

# define img1's color 
blue, green, red = cv.split(img1)
# extract color into blue 
blueimg = cv.merge([blue, zero, zero])
# show image then save in jpg file 
# cv.imwrite("valoblue.jpg", blueimg)

# define img1's color 
blue, green, red = cv.split(img2)
# extract color into green
greenimg = cv.merge([uno, green, uno])
# show image then save in jpg file 
# cv.imwrite("valogreen.jpg", greenimg)

# define img2's color 
blue, green, red = cv.split(img3)
# extract color into red 
redimg = cv.merge([tres, tres, red])
# show image then save in jpg file 
# cv.imwrite("valored.jpg", redimg)

## voila!! 
imagestack = cvzone.stackImages([redimg, blueimg, greenimg, img], 2, 0.8)
cv.imshow("stack", imagestack)
cv.imwrite("Tugas1.jpg", imagestack)
cv.imshow("rant_1", img)
cv.imshow("valoblue", blueimg)
cv.imshow("valogreen", greenimg)
cv.imshow("valored", redimg)


cv.waitKey(0)
cv.destroyAllWindows()