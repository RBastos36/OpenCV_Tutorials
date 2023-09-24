
# Template Matching

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('/home/rantonio/Desktop/messi.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# img2 = img.copy()
# template = cv.imread('/home/rantonio/Desktop/messi_face.jpg', cv.IMREAD_GRAYSCALE)
# assert template is not None, "file could not be read, check with os.path.exists()"
# w, h = template.shape[::-1]

# # All the 6 methods for comparison in a list
# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)

#     # Apply template Matching
#     res = cv.matchTemplate(img, template ,method)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)

#     cv.rectangle(img, top_left, bottom_right, 255, 2)
    
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()

# -------------------------------------------------------------------

# Template Matching with Multiple Objects

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv.imread('/home/rantonio/Desktop/mario.png')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

template = cv.imread('/home/rantonio/Desktop/mario_coin.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pnt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pnt, (pnt[0] + w, pnt[1] + h), (0,0,255), 2)

cv.imwrite('res.png',img_rgb)
cv.imshow("", res)
cv.waitKey(0)
cv.destroyAllWindows()
