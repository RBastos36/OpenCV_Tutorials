
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/rantonio/Desktop/coins.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

cv.imshow("Threshold", thresh)

# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations = 2)

# sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)
cv.imshow("Sure Background", sure_bg)

# Finding sure foreground area
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
cv.imshow("Distance Transform", dist_transform)
cv.imshow("Sure Foreground", sure_fg)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
cv.imshow("Unknown Area", unknown)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers += 1

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0
#### Figure out how to show the markers in JET colormap

markers = cv.watershed(img, markers)
img[markers == -1] = [255,0,0]

### Figure out how to show the markers in JET colormap
cv.imshow("Result", img)

cv.waitKey(0)
cv.destroyAllWindows()
