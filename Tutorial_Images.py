
import cv2 as cv
import sys

img = cv.imread("/home/rantonio/Desktop/sword_cemetery.jpeg")

if img is None:
    sys.exit

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("/home/rantonio/Desktop/sword_cemetery2.jpeg", img)

