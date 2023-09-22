
# Simple Thresholding

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread("/home/rantonio/Desktop/gradient.png", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
# ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray", vmin=0, vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

# ----------------------------------------------

# Simple Thresholding

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plot

# img = cv.imread("/home/rantonio/Desktop/sudoku.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# img = cv.medianBlur(img, 5)

# ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# titles = ['Original Image', 'Global Thresholding (v = 127)',
#           'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]

# for i in range(4):
#     plot.subplot(2, 2, i + 1), plot.imshow(images[i], "gray")
#     plot.title(titles[i])
#     plot.xticks([]), plot.yticks([])

# plot.show()

# ----------------------------------------------

# Otsu's Binarization

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plot

# img = cv.imread("/home/rantonio/Desktop/noisy1.png", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file coud not be read, check with os.path.exists()"

# # Global Thresholding
# ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# # Otsu's Thresholding
# ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# # Otsu's Thresholding after Gaussian filtering
# blur = cv.GaussianBlur(img, (5, 5), 0)
# ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# # Plot all images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# for i in range(3):
#     plot.subplot(3, 3, i * 3 + 1), plot.imshow(images[i * 3], 'gray')
#     plot.title(titles[i * 3]), plot.xticks([]), plot.yticks([])
#     plot.subplot(3, 3, i * 3 + 2), plot.hist(images[i * 3].ravel(), 256)
#     plot.title(titles[i * 3 + 1]), plot.xticks([]), plot.yticks([])
#     plot.subplot(3, 3, i * 3 + 3), plot.imshow(images[i * 3 + 2], 'gray')
#     plot.title(titles[i * 3 + 2]), plot.xticks([]), plot.yticks([])
# plot.show()

# ----------------------------------------------

# Otsu's Binarization Explanation

import cv2 as cv
import numpy as np

img = cv.imread('/home/rantonio/Desktop/noisy1.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
blur = cv.GaussianBlur(img, (5, 5), 0)

# find normalized_histogram, and its cumulative distribution function
hist = cv.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.sum()
Q = hist_norm.cumsum()

bins = np.arange(256)

fn_min = np.inf
thresh = -1

for i in range(1,256):
    p1, p2 = np.hsplit(hist_norm, [i]) # probabilities
    q1, q2 = Q[i], Q[255] - Q[i] # cum sum of classes
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    b1, b2 = np.hsplit(bins, [i]) # weights

    # finding means and variances
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print("Thresh: {}; Ret: {}".format(thresh, ret))
