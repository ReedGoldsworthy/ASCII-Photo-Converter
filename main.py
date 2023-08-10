import numpy as np
import cv2 
import sys

import colorama
from colorama import Fore, Back, Style

# Contrast on a scale -10 -> 10
contrast = 10
density = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|'
           '()1{}[]?-_+~<>i!lI;:,"^`\'.            ')
density = density[:-11+contrast]
n = len(density)

#gets image name from user
img_name = sys.argv[1]

try:
    width = int(sys.argv[2])
except IndexError:
    # Default ASCII image width.
    width = 100

# Read in the image, convert to greyscale.
gray_img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

# Resize the image as required.
orig_width, orig_height = gray_img.shape
r = orig_height / orig_width

# The ASCII character glyphs are taller than they are wide. Maintain the aspect
# ratio by reducing the image height.
height = int(width * r * 0.5)

gray_img = cv2.resize(gray_img, (width, height), fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

# prints the ascii character based off brightness value of the grayscale image
for i in range(height):
    for j in range(width):
        p = gray_img[i,j]
        k = int(np.floor(p/256 * n))
        print(density[ (n-1-k)], end='')
    print()