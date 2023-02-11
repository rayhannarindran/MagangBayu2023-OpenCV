import cv2 as cv
import numpy as np

def getBoundRect(contour):
    minx,miny,maxx,maxy = (contour[0][0][0],contour[0][0][1],contour[0][0][0],contour[0][0][1])

    for point in contour:
        x,y = point[0][0], point[0][1]
        if x<minx:minx=x
        if y<miny:miny=y
        if x>maxx:maxx=x
        if y>maxy:maxy=y
    
    midx = int((minx+maxx)/2)
    midy = int((miny+maxy)/2)

    return ((minx,miny),(maxx,maxy),(midx,midy))

#read the image
img= cv.imread('Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas2/tugas2.jpg')

hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV) #convert src to hsv colorspace
mask = cv.inRange(hsv,(150,100,240),(170,180,255)) #detect the square color
cnt, hierarchy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) #get the mask's contour

#obtain the bounding rectangle points' coordinates
rect = getBoundRect(cnt[0])

#draw the enclosing rectangle
cv.rectangle(img,rect[0],rect[1],(0,0,0),4)

#draw the midpoint
mid = rect[2]
cv.rectangle(img,mid,mid,(0,0,255),10) 

#draw the midpoint label text
text = f"Midpoint: (x:{mid[0]}, y:{mid[1]})"
org = (mid[0]-int(len(text)*5.5),mid[1]-20)
cv.putText(img,text,org,2,0.7,(0,0,0),lineType=cv.LINE_AA)

#render the image
cv.imshow('result',img)
cv.waitKey(0)
cv.destroyAllWindows()

#write the image
cv.imwrite("Achmad Iqbal Akbari_5022221118_TugasOpenCV/Tugas2/tugas2_done.jpg",img)