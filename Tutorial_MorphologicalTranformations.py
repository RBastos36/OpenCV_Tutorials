
import cv2 as cv
import numpy as np

img = cv.imread("/home/rantonio/Desktop/j.png", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow("erosion", erosion)
cv.imshow("dilation", dilation)
cv.imshow("opening", opening)
cv.imshow("closing", closing)
cv.imshow("gradient", gradient)
cv.imshow("tophat", tophat)
cv.imshow("blackhat", blackhat)
cv.waitKey(0)
cv.destroyAllWindows()
