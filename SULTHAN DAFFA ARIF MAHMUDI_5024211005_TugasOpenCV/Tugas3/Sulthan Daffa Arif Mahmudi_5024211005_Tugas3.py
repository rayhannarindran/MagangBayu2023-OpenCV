import cv2 as cv
import numpy as np

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

    # Blur image to remove noise
    gray = cv.GaussianBlur(gray, (5, 5), 0)

    # Find image edges
    edge = cv.Canny(gray, 50, 100)

    # Find contours
    contours, hierarchy = cv.findContours(edge, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Loop every contour
    for cnt in contours:
        # Epsilon
        epsilon = 0.01*cv.arcLength(cnt,True)
        # Poly Approximation
        approx = cv.approxPolyDP(cnt,epsilon,True)

        # Check if contour has 12 points/sides
        if len(approx) == 12:
            # Draw contour boundaries
            img = cv.drawContours(img, [cnt], -1, (0, 0, 255), 2)

            # Point count
            i = 0

            # Loop every point
            for pnt in approx:
                # Increment point count
                i += 1

                # Draw dot on the point
                cv.circle(img, pnt[0], 3, (0, 255, 0), -1)

                # Draw current point count on the point
                cv.putText(img, str(i), pnt[0], FONT, 0.4, (0, 0, 0), 1.25)
                
            # Draw total point count on top left of image
            cv.putText(img, str(i), (0, 50), FONT, 2, (0, 0, 255), 5)

            # Close loop to prevent duplicate contour
            break


    # Save / write image
    cv.imwrite(OUTPUT_PATH, img)

if __name__ == "__main__":
    main()