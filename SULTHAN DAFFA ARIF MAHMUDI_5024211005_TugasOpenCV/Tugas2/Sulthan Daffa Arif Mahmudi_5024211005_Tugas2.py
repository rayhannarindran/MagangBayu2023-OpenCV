import cv2 as cv
import numpy as np

import math

import argparse

INPUT_PATH = "./input/input.jpg"
OUTPUT_PATH = "./output/output.jpg"
FONT = cv.FONT_HERSHEY_SIMPLEX

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Input path")
    parser.add_argument("-o", "--output", type=str, help="Output path")
    args = parser.parse_args()

    global INPUT_PATH
    if args.input != None:
        INPUT_PATH = args.input

    global OUTPUT_PATH
    if args.output != None:
        OUTPUT_PATH = args.output

    # Read image
    img = cv.imread(INPUT_PATH)

    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to remove noise
    gray = cv.GaussianBlur(gray, (5, 5), 0)

    # Loop grayscale value from 0 to 255 with increament of 5
    for g in range(0, 250, 5):
        # Filter image to isolate certain gray value
        filtered = cv.inRange(gray, g, g + 5)

        # Find image edges
        edge = cv.Canny(filtered, 10, 20)

        # Find Contours
        contours, hierarchies = cv.findContours(edge, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        # Loop in every contour
        for cnt in contours:
            # Contour top left position
            x1,y1 = cnt[0][0]
            # Epsilon
            epsilon = 0.1*cv.arcLength(cnt,True)
            # Poly Approximation
            approx = cv.approxPolyDP(cnt,epsilon,True)

            # Check if countour has 4 sides (is square or rectangle)
            if len(approx) == 4:
                # Get countour origin x, y and width, height
                x, y, w, h = cv.boundingRect(cnt)

                # Check if contour width and height has approximately same value (is square)
                # And check if contour is big enough to be noticable
                if math.isclose(w, h, rel_tol=0.01) and w >= 10:
                    # Draw contour in original image
                    img = cv.drawContours(img, [cnt], -1, (0,0,0), 3)

                    # Get center of contour
                    center = (x + int(w/2), y + int(h/2))

                    # Draw dot in the center of contour
                    cv.circle(img, center, 5, (0, 0, 255), -1)

                    # String contains center position of contour
                    text = "Center: (%i, %i)" % (x + int(w/2), y + int(h/2))
                    # Get text size
                    textsize = cv.getTextSize(text, FONT, 0.6, 2)[0]
                    # Set text position to align to center of text
                    textpos = (int(center[0] - textsize[0]/2), int(center[1] - textsize[1]))

                    # Draw text in the center of contour
                    cv.putText(img, text, textpos, FONT, 0.6, (0, 0, 0), 2)

    # Save / write image
    cv.imwrite(OUTPUT_PATH, img)

if __name__ == "__main__":
    main()