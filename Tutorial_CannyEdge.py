
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# edges = cv.Canny(img, 100, 200, L2gradient=True)

# plt.subplot(121), plt.imshow(img, cmap="gray")
# plt.title("Original Image"), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap="gray")
# plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

# plt.show()

# ----------------------------------------------------------------

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


minVal = 100
maxVal = 200
eqt = 1
state = True


def nothing(x):
    pass


img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

edges = cv.Canny(img, minVal, maxVal, L2gradient=True)
cv.namedWindow("Edge Image")

cv.createTrackbar("Max","Edge Image" , 200, 255, nothing)
cv.createTrackbar("Min","Edge Image" , 100, 255, nothing)
cv.createTrackbar("L2Gradient","Edge Image" , 1, 1, nothing)

cv.imshow("Original Image", img)

while True:
    cv.imshow("Edge Image", edges)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    maxVal = cv.getTrackbarPos("Max", "Edge Image")
    minVal = cv.getTrackbarPos("Min", "Edge Image")
    eqt = cv.getTrackbarPos("L2Gradient", "Edge Image")
    if eqt == 1:
        state = True
    else:
        state = False

    edges = cv.Canny(img, minVal, maxVal, L2gradient=True)

cv.imshow("Original Image", img)

cv.destroyAllWindows()
