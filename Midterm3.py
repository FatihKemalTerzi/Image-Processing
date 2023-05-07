# -*- coding: utf-8 -*-
"""

@author: Fatih Kemal Terzi
"""

import cv2
import numpy as np

# Image reading
img = cv2.imread('pools.png')
count=0
# Image converting to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Adjusting range of blue color for detecting pools
lower_blue = np.array([80,50,50])
upper_blue = np.array([115,255,255])

# To spesifiying blue region creating binary mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Perform morphological operations to reduce noise
kernel = np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Find contours of blue regions
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around the blue regions
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    count+=1
# Display the result
cv2.imshow('Detected_pools', img)
print('Number of pools : ',count)
cv2.waitKey(0)
cv2.destroyAllWindows()
