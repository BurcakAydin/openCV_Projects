import cv2
import numpy as py
image = cv2.imread('keanuReeves.jpg', 0)

"""
image = cv2.imread('keanuReeves.jpg')

grayedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width, channel_N = image.shape
print("Original", height, width, channel_N)

height2, width2 = grayedImage.shape
print("Grayed", height2, width2)

cv2.imshow('Original', image)
cv2.imshow('Grayed', grayedImage)
"""
cv2.imshow('Grayed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
