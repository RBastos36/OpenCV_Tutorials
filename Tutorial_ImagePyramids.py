
# import cv2 as cv
# import numpy as np

# img = cv.imread("/home/rantonio/Desktop/messi.jpg")
# assert img is not None, "file could not be read, check with os.path.exists()"

# lower_res = cv.pyrDown(img)
# lower_res = cv.pyrDown(lower_res)
# lower_res = cv.pyrDown(lower_res)
# higher_res = cv.pyrUp(lower_res)
# higher_res = cv.pyrUp(higher_res)
# higher_res = cv.pyrUp(higher_res)

# cv.imshow("lower_res", lower_res)
# cv.imshow("higher_res", higher_res)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ---------------------------------------------------------

# Image Blending using Pyramids

import cv2 as cv
import numpy as np,sys

A = cv.imread('/home/rantonio/Desktop/apple.png')
B = cv.imread('/home/rantonio/Desktop/orange.png')
assert A is not None, "file could not be read, check with os.path.exists()"
assert B is not None, "file could not be read, check with os.path.exists()"
A = cv.resize(A, (512, 512))
B = cv.resize(B, (512, 512))

# Generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
   G = cv.pyrDown(G)
   gpA.append(G)
   
# Generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
   G = cv.pyrDown(G)
   gpB.append(G)
   
# Generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
   GE = cv.pyrUp(gpA[i])
   L = cv.subtract(gpA[i - 1], GE)
   lpA.append(L)

# Generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
   GE = cv.pyrUp(gpB[i])
   L = cv.subtract(gpB[i - 1], GE)
   lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
   rows, cols, dpt = la.shape
   ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
   LS.append(ls)

# Now reconstruct
ls_ = LS[0]
for i in range(1,6):
   ls_ = cv.pyrUp(ls_)
   ls_ = cv.add(ls_, LS[i])

# Image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

cv.imshow('Pyramid_blending.jpg',ls_)
cv.imshow('Direct_blending.jpg',real)
cv.waitKey(0)
cv.destroyAllWindows()

