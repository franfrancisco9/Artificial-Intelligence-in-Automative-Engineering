import numpy as np

import matplotlib.pyplot as plt

import cv2

# Read in the image

image = cv2.imread('Example_Picture.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Grab the x and y size and make a copy of the image

ysize = image.shape[0]

xsize = image.shape[1]

color_select = np.copy(image)

# Define color selection criteria to only get the white lines
# Get the optimal RGB values for the white lines


red_threshold = 190

green_threshold = 190

blue_threshold = 180

rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Do a boolean or with the "|" character to identify pixels below the thresholds

thresholds = (image[:,:,0] < rgb_threshold[0])   | (image[:,:,1] < rgb_threshold[1])    | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0, 0, 0]


# Display the image                

plt.imshow(color_select)
#save image
plt.savefig('Example_Picture_white.jpg')
#plt.show()