
# 2D Convolution

# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plot

# img = cv.imread("/home/rantonio/Desktop/messi.jpg")
# assert img is not None, "file could not be read, check with os.path.exists()"

# kernel = np.ones((5, 5,), np.float32) / 25
# dst = cv.filter2D(img, -1, kernel)

# plot.subplot(121), plot.imshow(img), plot.title("Original")
# plot.xticks([]), plot.yticks([])
# plot.subplot(122), plot.imshow(dst), plot.title("Averaging")
# plot.xticks([]), plot.yticks([])
# plot.show()

# --------------------------------------------------------

# Image Blurring

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

img = cv.imread('/home/rantonio/Desktop/messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# blur = cv.blur(img,(5, 5))                                                # Averaging
# blur = cv.boxFilter(src=img, ksize=(5, 5), ddepth=-1, normalize=False)    # Averaging
# blur = cv.GaussianBlur(img, (5, 5), 0)                                    # Gaussian Blurring
# blur = cv.medianBlur(img,5)                                               # Median Blurring
blur = cv.bilateralFilter(img, 9, 75, 75)                                   # Bilateral Filtering

plot.subplot(121),plot.imshow(img),plot.title('Original')
plot.xticks([]), plot.yticks([])
plot.subplot(122),plot.imshow(blur),plot.title('Blurred')
plot.xticks([]), plot.yticks([])
plot.show()
