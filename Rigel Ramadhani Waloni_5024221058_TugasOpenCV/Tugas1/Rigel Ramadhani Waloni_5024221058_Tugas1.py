# Import the Required Libraries
import cv2 as cv

# Read the Image
img = cv.imread("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas1/tugas1.jpg")

# Converting the Color Space
img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img_LUV = cv.cvtColor(img, cv.COLOR_BGR2LUV)
img_HLS = cv.cvtColor(img, cv.COLOR_BGR2HLS)

# Cropping Image
imgPART1 = img[0:125, 0:200]
imgPART2 = img_RGB[0:125, 200:400]
imgPART3 = img_HSV[0:125, 400:600]
imgPART4 = img_LUV[0:125, 600:800]

imgPART5 = img_LUV[125:250, 0:200]
imgPART6 = img[125:250, 200:400]
imgPART7 = img_RGB[125:250, 400:600]
imgPART8 = img_HSV[125:250, 600:800]

imgPART9 = img_HSV[250:375, 0:200]
imgPART10 = img_LUV[250:375, 200:400]
imgPART11 = img[250:375, 400:600]
imgPART12 = img_RGB[250:375, 600:800]

imgPART13 = img_RGB[375:500, 0:200]
imgPART14 = img_HSV[375:500, 200:400]
imgPART15 = img_LUV[375:500, 400:600]
imgPART16 = img[375:500, 600:800]

# Join the Parts
combinedP1 = cv.hconcat([imgPART1, imgPART2, imgPART3, imgPART4])
combinedP2 = cv.hconcat([imgPART5, imgPART6, imgPART7, imgPART8])
combinedP3 = cv.hconcat([imgPART9, imgPART10, imgPART11, imgPART12])
combinedP4 = cv.hconcat([imgPART13, imgPART14, imgPART15, imgPART16])

# Join All Parts
combineAll = cv.vconcat([combinedP1, combinedP2, combinedP3, combinedP4])

# Display the Combined Parts and Original Image
cv.imshow("FINAL | 16 PARTS OF IMAGES WITH DIFFERENT COLOR SPACE", combineAll)
cv.imshow("ORIGINAL", img)

# Create a Final Image
cv.imwrite("Rigel Ramadhani Waloni_5024221058_TugasOpenCV/Tugas1/tugas1_done.jpg", combineAll)

cv.waitKey(0)
cv.destroyAllWindows()