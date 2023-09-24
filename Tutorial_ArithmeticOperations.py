
# import cv2 as cv
# import numpy as np

# img1 = cv.imread('/home/rantonio/Desktop/sword_cemetery.jpeg')
# img2 = cv.imread('/home/rantonio/Desktop/messi.jpg')

# img1 = cv.resize(img1, (1000, 700))
# img2 = cv.resize(img2, (1000, 700))

# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"

# dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ----------------------------------------------------------

# import cv2 as cv
# import numpy as np

# # Load two images
# img1 = cv.imread('/home/rantonio/Desktop/messi.jpg')
# img2 = cv.imread('/home/rantonio/Desktop/sword_cemetery.jpeg')

# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"

# # I want to put logo on top-left corner, So I create a ROI
# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]

# # Now create a mask of logo and create its inverse mask also
# img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# ret, mask = cv.threshold(img2gray, 240, 250, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)
# cv.imshow('res0', img2gray)
# cv.imshow('res00', mask_inv)

# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
# cv.imshow('res1', img1_bg)

# # Take only region of logo from logo image.
# img2_fg = cv.bitwise_and(img2, img2, mask = mask)
# cv.imshow('res2', img2_fg)

# # Put logo in ROI and modify the main image
# dst = cv.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst

# cv.imshow('res', img1)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -------------------------------------------------

import cv2 as cv
import numpy as np 
import os

img_main = np.zeros((500,500,3), np.uint8)

location = "/home/rantonio/Desktop/Images2 "

for file in os.listdir(location):  
    img = cv.imread(location + '/' + file)

    for alpha in range(1, 11):
        alpha = alpha / 10
        beta = 1 - alpha
        cv.imshow('SlideShow', cv.addWeighted(img, alpha, img_main, beta, 0.0))
        cv.waitKey(50)

    if cv.waitKey(0) & 0xFF == ord('q'):
        break
    img_main = img

cv.destroyAllWindows()
