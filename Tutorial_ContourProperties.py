
import numpy as np
import cv2 as cv

img = cv.imread("/home/rantonio/Desktop/lightening.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
countours, hierarchy = cv.findContours(thresh, 1, 2)

cnt = countours[0]

x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w) / h
print(aspect_ratio)

area = cv.contourArea(cnt)
x, y, w, h = cv.boundingRect(cnt)
rect_area = w * h
extent = float(area)/rect_area
print(extent)

area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area) / hull_area
print(solidity)

area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
print(equi_diameter)

(x, y), (MA, ma), angle = cv.fitEllipse(cnt)
print(angle)

mask = np.zeros(imgray.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)
# pixelpoints = np.transpose(np.nonzero(mask))
pixelpoints = cv.findNonZero(mask)
print(pixelpoints)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray, mask = mask)
print("{}; {}; {}; {}".format(min_val, max_val, min_loc, max_loc))

mean_val = cv.mean(img, mask = mask)
print(mean_val)

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print("L: {}; R: {}; T: {}; B:{}".format(leftmost, rightmost, topmost, bottommost))
