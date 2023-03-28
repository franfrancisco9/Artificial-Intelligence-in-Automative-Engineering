import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Rescale the images
    frame = cv2.resize(frame, (0, 0), None, .70, .70)

    # Change color spaces
    bgr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.dstack([gray, gray, gray])

    # Put all images in one numpy stack
    output = np.hstack((frame, bgr, gray))

    # Display the resulting frame and quit with 'q'
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
