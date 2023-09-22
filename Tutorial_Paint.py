
import numpy as np
import cv2 as cv

drawing = False     # true if mouse is pressed
mode = True         # if true, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        print("Started Drawing")
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), rad)
                print("Drawn a Rectangle")
            else:
                cv.circle(img, (x, y), rad, (b, g, r), -1)
                print("Drawn a Circle")

    
    if event == cv.EVENT_LBUTTONUP:
        drawing = False
        print("Ended Drawing")


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image", draw_circle)

# Create trackbars for Paint Brush color change
cv.createTrackbar("R", "image", 0, 255, nothing)
cv.createTrackbar("G", "image", 0, 255, nothing)
cv.createTrackbar("B", "image", 0, 255, nothing)

# Create trackbars for Paint Brush radius change
cv.createTrackbar("Radius", "image", 0, 10, nothing)

while True:
    cv.imshow("image", img)
    k = cv.waitKey(1) & 0xFF

    if k == ord("m"):
        mode = not mode
    elif k == 27:
        break

    # Get current positions of four trackbars
    r = cv.getTrackbarPos("R", "image")
    g = cv.getTrackbarPos("G", "image")
    b = cv.getTrackbarPos("B", "image")
    rad = cv.getTrackbarPos("Radius", "image")


cv.destroyAllWindows()
