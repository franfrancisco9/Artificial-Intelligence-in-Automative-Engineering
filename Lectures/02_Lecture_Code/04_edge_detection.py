import numpy as np
import cv2


filter_size = (5, 5)
lower_threshold = 30
upper_threshold = 80

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Transform to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, filter_size, cv2.BORDER_DEFAULT)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, lower_threshold, upper_threshold)

    # Put all images in one numpy stack
    output = np.hstack((gray, edges))

    # Display the resulting frame and quit with 'q'
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
