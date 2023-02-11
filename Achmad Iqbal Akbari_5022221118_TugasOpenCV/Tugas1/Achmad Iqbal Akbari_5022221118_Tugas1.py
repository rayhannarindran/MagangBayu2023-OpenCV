import cv2 as cv
import numpy as np
from random import randint as rand

#read the image
src = cv.imread('Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas1/tugas1.jpg')

#setting up the filter mask
height,width = (src.shape[0],src.shape[1])
mask = np.zeros((height,width,3),np.uint8)

#applying the filter
r,c = (3,4) # the amount of rows and columns to partition the filter mask
for i in range(0,r+1):
    for j in range(0,c+1):
        color = (rand(0,255),rand(0,255),rand(0,255))
        
        cv.rectangle(mask, ((i)*int(width/r), (j)*int(height/c)),((i+1)*int(width/r),(j+1)*int(height/c)), color, -1)
        dst = cv.add(src,mask)

#show the image
cv.imshow("source",cv.resize(src,(int(width/6),int(height/6))))
cv.imshow("result",cv.resize(dst,(int(width/6),int(height/6))))
cv.waitKey(0)
cv.destroyAllWindows()

#write the image
cv.imwrite("Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas1/tugas1_done.jpg",dst)