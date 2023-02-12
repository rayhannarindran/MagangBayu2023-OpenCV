import cv2 as cv
import numpy as np

import os
import argparse

import random

INPUT_PATH = "./input/input.jpg"
OUTPUT_PATH = "./output/output.jpg"
HORIZONTAL_PARTITION = 3
VERTICAL_PARTITION = 2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Input path")
    parser.add_argument("-o", "--output", type=str, help="Output path")
    parser.add_argument("--vertical-partition", type=int, help="How much vertical partition")
    parser.add_argument("--horizontal-partition", type=int, help="How much horizontal partition")
    args = parser.parse_args()

    global INPUT_PATH
    if args.input != None:
        INPUT_PATH = args.input

    global OUTPUT_PATH
    if args.output != None:
        OUTPUT_PATH = args.output

    global HORIZONTAL_PARTITION
    if args.horizontal_partition != None:
        HORIZONTAL_PARTITION = args.horizontal_partition

    global VERTICAL_PARTITION
    if args.vertical_partition != None:
        VERTICAL_PARTITION = args.vertical_partition

    Recolor()

def Recolor():
    # Read Image
    img = cv.imread(INPUT_PATH)
    # Change image type to HSV
    img = cv.cvtColor(img, cv.COLOR_RGB2HSV)

    # Get image height & width
    height, width = img.shape[:2]

    # Get Partition height & width
    height = int(height / VERTICAL_PARTITION)
    width = int(width / HORIZONTAL_PARTITION)

    # Initialize partitions list as 2D list
    result_list = []

    # Loop vertical partitions
    for v in range(0, VERTICAL_PARTITION):
        # Initialize horizontal partitions list
        cropped_list = []

        # Loop horizontal partitions
        for h in range(0, HORIZONTAL_PARTITION):
            # Crop image from (height * v, width * h) to (height * (v + 1), width * (h + 1))
            # to get image of each partition
            cropped = img[height * v:height * (v + 1), width * h:width * (h + 1)]

            # Get randomized hue value
            # Hue ranges between 0 to 180
            hue = random.randint(0, 180)

            # Assign hue value to partition image
            cropped[:,:,0] = hue

            # Append partition image to horizontal partitions list
            cropped_list.append(cropped)

        # Append horizontal partitions list to 2D partitions list
        result_list.append(cropped_list)

    # Concatenate / combine partition images to create single image
    result = cv.vconcat([cv.hconcat(list_h) 
                        for list_h in result_list])

    # Convert image result back to RGB
    result = cv.cvtColor(result, cv.COLOR_HSV2RGB)

    # Save image
    cv.imwrite(OUTPUT_PATH, result)

if __name__ == "__main__":
    main()