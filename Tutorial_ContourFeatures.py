
# import numpy as np
# import cv2 as cv

# img = cv.imread("/home/rantonio/Desktop/blackandwhite.png")
# assert img is not None, "file could not be read, check with os.path.exists()"
# imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# countours, hierarchy = cv.findContours(thresh, 1, 2)

# cnt = countours[0]
# M = cv.moments(cnt)
# print(M)

# cx = int(M['m10'] / M['m00'])
# cy = int(M['m01'] / M['m00'])

# print(cx)
# print(cy)

# area = cv.contourArea(cnt)
# perimeter = cv.arcLength(cnt, True)

# print("Area: {}\nPerimeter: {}".format(area, perimeter))

# # epsilon = 0.001 * cv.arcLength(cnt, True)
# # approx = cv.approxPolyDP(cnt, epsilon, True)
# # cv.drawContours(img, approx, -1, (255, 0, 255), 3)

# # hull = cv.convexHull(cnt)
# # cv.drawContours(img, hull, -1, (255, 0, 255), 3)

# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -----------------------------------------------------

import numpy as np
import cv2 as cv

img = cv.imread("/home/rantonio/Desktop/lightening.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
countours, hierarchy = cv.findContours(thresh, 1, 2)

cnt = countours[0]

x, y, w, h = cv.boundingRect(cnt)
cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)

(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img, center, radius, (0, 255, 0), 2)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (0, 255, 0), 2)

rows, cols = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
