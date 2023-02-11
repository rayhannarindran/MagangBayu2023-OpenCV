import cv2 as cv

#reading image, resizing
img = cv.imread("tugas3.jpg")
img = cv.resize(img, (800,450))

#change to gray color, blurring, and canny to do countour
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurr = cv.GaussianBlur(img, (5, 5), 0)
canny = cv.Canny(blurr, 125, 175)

#countours and its hierarchy, generate the 'H' countour
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
h_contour = min(contours, key=cv.contourArea)

# draw contour
contour = img.copy()
cv.drawContours(contour, [h_contour], 0, (0,0,255), 2)

# get number of vertices (sides)
peri = cv.arcLength(h_contour, True)
approx = cv.approxPolyDP(h_contour, 0.02 * peri, True)

#putting text on the picture
num = str(len(approx))
cv.putText(contour, num, (20, 35), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

#make the result as a .jpg file and show
cv.imwrite("tugas3_done.jpg",contour)
cv.imshow("pict", img)
cv.imshow("contour", contour)
cv.waitKey(0)
cv.destroyAllWindows()