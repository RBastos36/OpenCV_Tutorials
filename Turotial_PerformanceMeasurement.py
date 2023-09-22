
import cv2 as cv
from time import time


# e1 = cv.getTickCount()
# # your code execution
# e2 = cv.getTickCount()
# time = (e2 - e1)/ cv.getTickFrequency()
# print(time)

img1 = cv.imread("/home/rantonio/Desktop/messi.jpg")
assert img1 is not None, "file could not be read, check with os.path.exists()"

e1 = cv.getTickCount()
e1_1 =time()

for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1,i)

e2 = cv.getTickCount()
e2_2 = time()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
print(e2_2 - e1_1)
