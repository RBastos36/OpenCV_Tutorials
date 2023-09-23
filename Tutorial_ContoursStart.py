
import cv2 as cv
import numpy as np

img = cv.imread("/home/rantonio/Desktop/square.jpg")
assert img is not None, "file could no tbe read, check with os.path.exists()"

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 255, 255), 3)
# cv.drawContours(img, contours, 3, (0,255,0), 3)
# cnt = contours[0]
# cv.drawContours(img, [cnt], 0, (0,255,0), 3)

cv.imshow("countour", img)
cv.waitKey(0)
cv.destroyAllWindows()
