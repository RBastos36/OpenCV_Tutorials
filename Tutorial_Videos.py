
# Capture Video from Camera

import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera!")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Print the frame width and height
    print(str(cap.get(cv.CAP_PROP_FRAME_WIDTH)) + " , " + str(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

    # if frame is correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)

    if cv.waitKey(100) == ord('q'):
        break

    # Set new frame width and height
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
