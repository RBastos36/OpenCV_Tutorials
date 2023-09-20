
# # Capture Video from Camera

# import cv2 as cv


# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera!")
#     exit()

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     # Print the frame width and height
#     print(str(cap.get(cv.CAP_PROP_FRAME_WIDTH)) + " , " + str(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

#     # if frame is correctly, ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
    
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv.imshow('frame', gray)

#     if cv.waitKey(10) == ord('q'):
#         break

#     # Set new frame width and height
#     ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
#     ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)

# # When everything is done, release the capture
# cap.release()
# cv.destroyAllWindows()

# ----------------------------------------------------------------------

# Playing Video from file

# import numpy as np
# import cv2 as cv

# cap = cv.VideoCapture("/home/rantonio/Desktop/memes.mp4")

# while cap.isOpened():
#     ret, frame = cap.read()

#     # if frame is read correctly, ret is True
#     if not ret:
#         print("Can't retrieve frame(stream end?). Exiting ...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     cv.imshow("frame", gray)
#     if cv.waitKey(25) == ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()

# ----------------------------------------------------------------------

# Saving a Video

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)

    # Write the flipped frame
    out.write(frame)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

