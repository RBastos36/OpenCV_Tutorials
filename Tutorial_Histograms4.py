
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# #roi is the object or region of object we need to find
# roi = cv.imread('/home/rantonio/Desktop/messi.jpg')
# assert roi is not None, "file could not be read, check with os.path.exists()"
# hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# #target is the image we search in
# target = cv.imread('/home/rantonio/Desktop/messi.jpg')
# assert target is not None, "file could not be read, check with os.path.exists()"
# hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# # Find the histograms using calcHist. Can be done with np.histogram2d also
# M = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# I = cv.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256] )

# R = np.divide(M, I)

# h, s, v = cv.split(hsvt)
# B = R[h.ravel(),s.ravel()]
# B = np.minimum(B,1)
# B = B.reshape(hsvt.shape[:2])

# disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# cv.filter2D(B, -1, disc, B)
# B = np.uint8(B)
# cv.normalize(B, B, 0, 255, cv.NORM_MINMAX)

# ret, thresh = cv.threshold(B, 50, 255, 0)

# ----------------------------------------------------------------

import numpy as np
import cv2 as cv

roi = cv.imread('/home/rantonio/Desktop/messi.jpg')
assert roi is not None, "file could not be read, check with os.path.exists()"
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

target = cv.imread('/home/rantonio/Desktop/messi.jpg')
assert target is not None, "file could not be read, check with os.path.exists()"
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 70, 220, 270])

# normalize histogram and apply backprojection
cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt], [0, 1], roihist, [0, 70, 220, 270], 1)

# Now convolute with circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
cv.filter2D(dst, -1, disc,dst)

# threshold and binary AND
ret, thresh = cv.threshold(dst, 50, 255, 0)
thresh = cv.merge((thresh, thresh,thresh))
res = cv.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv.imwrite('res.jpg', res)
