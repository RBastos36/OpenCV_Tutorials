
import cv2 as cv
import numpy as np

img = cv.imread('/home/rantonio/Desktop/lightening.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 2, 1)
cnt = contours[0]

hull = cv.convexHull(cnt, returnPoints = False)
defects = cv.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img, start, end, [0, 255, 0], 2)
    cv.circle(img, far, 5, [0, 0, 255], -1)

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        R = 255
        G = 255
        B = 255
        dist = cv.pointPolygonTest(cnt, (x, y), True)
        if dist == 0:
            cv.circle(img, (x, y), 2, (B, G, R), -1)
        elif dist > 0:
            # It lacks code to make red gradient...
            cv.circle(img, (x, y), 2, (0, 0, R), -1)
        elif dist < 0:
            # It lacks code to make blue gradient...
            cv.circle(img, (x, y), 2, (B, 0, 0), -1)

# print(img.shape[:2])

dist = cv.pointPolygonTest(cnt, (50, 50), True)
print(dist)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

# -----------------------------------------------------------

# import cv2 as cv
# import numpy as np

# img1 = cv.imread('/home/rantonio/Desktop/lightening.jpg', cv.IMREAD_GRAYSCALE)
# img2 = cv.imread('/home/rantonio/Desktop/square.jpg', cv.IMREAD_GRAYSCALE)
# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"

# ret, thresh = cv.threshold(img1, 127, 255, 0)
# ret, thresh2 = cv.threshold(img2, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, 2, 1)
# cnt1 = contours[0]
# contours, hierarchy = cv.findContours(thresh2, 2, 1)
# cnt2 = contours[0]

# ret = cv.matchShapes(cnt1, cnt2, 1, 0.0)
# print( ret )
