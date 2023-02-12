import cv2 as cv
import numpy as np

#read the image
img = cv.imread('Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas3/tugas3.jpg')

#create the mask
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) #convert src to hsv
mask = cv.inRange(hsv,(100,120,0),(140,240,255)) #detect the shape color

#sharpen the mask
kernel = np.ones((5, 5), np.uint8) #preparing the kernel
mask = cv.dilate(mask,kernel,iterations=1) #remove holes
mask = cv.erode(mask,kernel,iterations=3) #closing in
mask = cv.dilate(mask,kernel,iterations=3)
mask = cv.erode(mask,kernel,iterations=1) #undo the first dilation
cv.imshow('mask',mask)

#get the mask's contour
contour, hierarchy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

#draw the contour/border of the shape (get the third hierrachy)
cv.drawContours(img,contour,2,(0,0,255),4)

#merge nearby points into one
temp = contour[2]; i = 0; m = 1
for item in temp:
    if np.allclose(temp[i],temp[i-1],atol=2):
        m = m+1
        temp[i-1] = ((m-1)*temp[i-1]+temp[i])/m
        temp = np.delete(temp,i,0)
    else:
        i = i+1; m = 1

#print the amount of points
cv.putText(img,f"{len(temp)}",(30,100),5,4,color=(0,0,0),thickness=4,lineType=cv.LINE_AA)       
temp = np.array([temp],np.int32)

#show the result
cv.imshow('result',img)
cv.waitKey(0)
cv.destroyAllWindows()

#write the result
cv.imwrite('Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas3/tugas3_done.jpg',img)