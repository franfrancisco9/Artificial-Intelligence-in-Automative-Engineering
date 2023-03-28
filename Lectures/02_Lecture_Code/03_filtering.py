import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)

    # Define and apply sharpen kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(frame, -1, kernel)

    # Put all images in one numpy stack
    output = np.hstack((frame, blurred, sharpened))

    # Display the resulting frame and quit with 'q'
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
