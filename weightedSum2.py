import cv2
import numpy as np

image1 = cv2.imread("watch1.jpg")
image2 = cv2.imread('watch2.jpg')
imageSum = cv2.add(image1, image2)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)


cv2.imshow('Summed Images', imageSum)
cv2.imshow('Weighted Imgages', weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()
