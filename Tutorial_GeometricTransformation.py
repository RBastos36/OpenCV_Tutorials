
# Scaling

# import numpy as np
# import cv2 as cv

# img = cv.imread('/home/rantonio/Desktop/messi.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"

# # res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
# # OR
# height, width = img.shape[:2]
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

# cv.imshow('image',res)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -----------------------------------------------

# Translation

# import numpy as np
# import cv2 as cv

# img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# rows, cols = img.shape[:2]

# M = np.float32([[1, 0, 100],
#                 [0, 1, 50]])
# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow("image", dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -----------------------------------------------

# Rotation

# import numpy as np
# import cv2 as cv

# img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# rows, cols = img.shape[:2]

# M = cv.getRotationMatrix2D(((cols -1 ) / 2.0, (rows - 1) / 2.0), 90, 1)
# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow("image", dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -----------------------------------------------

# Affine Transformation

# import numpy as np
# import cv2 as cv

# img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# rows, cols = img.shape[:2]

# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# M = cv.getAffineTransform(pts1, pts2)
# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow("image", dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# -----------------------------------------------

# Perspective Transformation

import numpy as np
import cv2 as cv

img = cv.imread("/home/rantonio/Desktop/messi.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols = img.shape[:2]

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))

cv.imshow("image", dst)
cv.imshow("original", img)
cv.waitKey(0)
cv.destroyAllWindows()