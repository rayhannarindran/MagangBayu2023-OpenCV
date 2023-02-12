import cv2 as cv

img = cv.imread("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas1/tugas1.jpg")
# resize image
img = cv.resize(img, (1000,600))
# mengcopy image
baseImg = img.copy()
# membuat rectangle berisi warna yang telah ditentukan
cv.rectangle(img, (0,0),(500,300), (255,0,0), cv.FILLED)
cv.rectangle(img, (500,0),(1000,300), (0,255,0), cv.FILLED)
cv.rectangle(img, (0,300),(500,600), (0,0,255), cv.FILLED)
cv.rectangle(img, (500,300),(1000,600), (0,255,255), cv.FILLED)

# blending color with baseImg
cv.addWeighted(img, 0.5, baseImg, 0.7, 20, baseImg)
# menampilkan gambar
cv.imshow("image", baseImg)
# save image
cv.imwrite("Adnan Adbullah Juan_5025221155_TugasOpenCV/Tugas1/tugas1_done.jpg", baseImg)

cv.waitKey(0)
cv.destroyAllWindows()