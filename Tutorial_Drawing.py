import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

#Draw a diagonal blue with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a green rectangle at the top-right corner of image
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a circle inside the rectangle drawn above
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Draw a half ellipse at the center of the image
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw a small polygon of with four vertices in yellow color
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Write text on the image
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# Show image created above
cv.imshow("Image", img)

# Close image at keypress
if cv.waitKey(0) == ord("q"):
    cv.destroyAllWindows

#------------------------------------

# New image recreating OpenCV logo
img = np.zeros((500, 500, 3), np.uint8)

# Trying to draw with circles and polylines to delete the blanks
# cv.circle(img,(225, 120), 50, (0, 0, 255), 40)
# cv.circle(img,(150, 250), 50, (0, 255, 0), 40)
# cv.circle(img,(300, 250), 50, (255, 0, 0), 40)

# pts = np.array([[225, 120], [150, 250], [225, 250], [225, 120], [300, 250], [(300 + 150 / 2), 120], [150, 250]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv.polylines(img, [pts], True, (0, 0, 0), 1)

# cv.drawContours(img, pts, -1, (255, 255, 255), -1)

# cv.fillPoly(img, pts, (0, 0, 0))

# Drawn using ellipses with the measurements to make them circles
cv.ellipse(img, (256, 80), (60, 60), 120, 0, 300, (0, 0, 255), -1)
cv.ellipse(img, (256, 80), (20, 20), 120, 0, 360, (0, 0, 0), -1)
cv.ellipse(img, (176, 200), (60, 60), 0, 0, 300, (0, 255, 0), -1)
cv.ellipse(img, (176, 200), (20, 20), 0, 0, 360, (0, 0, 0), -1)
cv.ellipse(img, (336, 200), (60, 60), 300, 0, 300, (255, 0, 0), -1)
cv.ellipse(img, (336, 200), (20, 20), 300, 0, 360, (0, 0, 0), -1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (196, 296), font, 1, (255, 255, 255), 4, cv.LINE_AA)


cv.imshow("Image", img)
if cv.waitKey(0) == ord("q"):
    cv.destroyAllWindows