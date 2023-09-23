
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread('/home/rantonio/Desktop/wiki.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# hist,bins = np.histogram(img.flatten(), 256, [0,256])

# cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()

# cdf_m = np.ma.masked_equal(cdf, 0)
# cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')

# img2 = cdf[img]

# hist,bins = np.histogram(img2.flatten(), 256, [0,256])

# cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()

# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img2.flatten(), 256, [0, 256], color = 'r')
# plt.xlim([0, 256])
# plt.legend(('cdf', 'histogram'), loc = 'upper left')
# plt.show()

# cv.imshow("After Histograms Equalization", img2)
# cv.imshoy("Before Histograms Equalization", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ----------------------------------------------------

# import numpy as np
# import cv2 as cv

# img = cv.imread('/home/rantonio/Desktop/wiki.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# equ = cv.equalizeHist(img)
# res = np.hstack((img, equ)) #stacking images side-by-side
# cv.imwrite('res.png', res)

# ----------------------------------------------------

import numpy as np
import cv2 as cv
img = cv.imread('/home/rantonio/Desktop/tsukuba_l.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imwrite('clahe_2.jpg',cl1)