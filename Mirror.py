import cv2
import numpy as np

image = cv2.imread('adileNasit.jpg')

reflectedImage = cv2.copyMakeBorder(
    image, 200, 200, 200, 200, cv2.BORDER_REFLECT)
replicatedImage = cv2.copyMakeBorder(
    image, 200, 200, 200, 200, cv2.BORDER_REPLICATE)
wrappedImage = cv2.copyMakeBorder(
    image, 300, 300, 300, 300, cv2.BORDER_WRAP)
frameImage = cv2.copyMakeBorder(
    image, 300, 300, 300, 300, cv2.BORDER_CONSTANT, value=(75, 150, 255))

cv2.imshow('Adile Nasit', reflectedImage)
cv2.imshow('Longened Adile Nasit', replicatedImage)
cv2.imshow('Wrapped Adile Nasit', wrappedImage)
cv2.imshow('Framed Adile Nasit', frameImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
