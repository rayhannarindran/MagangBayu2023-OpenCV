import cv2 as cv

img = cv.imread('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas1/tugas1.jpg')
unedited_img = img.copy()

# x = img.shape[1] , y = img.shape[0]
top_left = cv.rectangle(img,(0,0),(img.shape[1]//2,img.shape[0]//2),(0,0,200),-1)
top_right = cv.rectangle(img,(img.shape[1]//2,0),(img.shape[1],img.shape[0]//2),(0,200,200),-1)
bottom_left = cv.rectangle(img,(0,img.shape[0]//2),(img.shape[1]//2,img.shape[0]),(0,200,0),-1)
bottom_right = cv.rectangle(img,(img.shape[1]//2,img.shape[0]//2),(img.shape[1],img.shape[0]),(200,0,0),-1) 

edited_img = img.copy()
# addWeighted for blending 2 images between unedited_img and edited_img
cv.addWeighted(unedited_img, 0.7, edited_img, 0.3, 1, img)
cv.imshow('Result', img)
# Save the image
cv.imwrite('Zelvan Abdi Wijaya_5025221125_TugasOpenCV/Tugas1/tugas1_done.jpg', img)
cv.waitKey(0)