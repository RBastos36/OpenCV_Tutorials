
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread('/home/rantonio/Desktop/messi.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# plt.plot(hist)
# plt.show()

# -------------------------------------------------------------

# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread('/home/rantonio/Desktop/messi.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# hist, xbins, ybins = np.histogram2d(hsv[0].ravel(), hsv[1].ravel(), [180,256], [[0,180], [0,256]])

# plt.plot(hist)
# plt.show()

# cv.imshow("", hist)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -------------------------------------------------------------

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/rantonio/Desktop/messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist, interpolation = 'nearest')
plt.show()
