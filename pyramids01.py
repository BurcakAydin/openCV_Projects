import cv2
import numpy as np

image = cv2.imread('kevinCostner.jpg')
resizedImage = cv2.pyrUp(image)
resizedImage2 = cv2.pyrDown(image)

cv2.imshow('Original', image)
cv2.imshow('Resized', resizedImage),
cv2.imshow('Resized', resizedImage2),

print('Original', image.shape)
print('Resized', resizedImage.shape)
print('Resized2', resizedImage2.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
