import numpy as np
import cv2


# Canny parameters
filter_size = (5, 5)
lower_threshold = 30
upper_threshold = 80

# Hough parameters
rho = 1
theta = np.pi / 180
hough_threshold = 20
min_line_length = 10
max_line_gap = 10

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

    # Hough transform
    lines = cv2.HoughLinesP(edges, rho, theta, hough_threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)

    # Create a blank to draw lines on
    line_image = np.copy(gray) * 0

    # Iterate over the output "lines" and draw lines on the blank
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

    # Put all images in one numpy stack
    output = np.hstack((gray, edges, line_image))

    # Display the resulting frame and quit with 'q'
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
