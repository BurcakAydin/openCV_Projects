import cv2 as cv
import numpy as np

image = cv.imread("kevinCostner.jpg")
kernel = np.ones((5, 5), np.uint8)
# dilation = cv.dilate(image, kernel, iterations=1)
erosion = cv.erode(image, kernel, iterations=1)
erosion2 = cv.erode(image, kernel, iterations=2)
""" 
dilation = cv.dilate(erosion, kernel, iterations=1)
dilation2 = cv.dilate(erosion, kernel, iterations=2)
cv.imshow("dilation", dilation)
cv.imshow("dilation2", dilation2)
"""

cv.imshow("original", image)
cv.imshow("erosion", erosion)
cv.imshow("erosion2", erosion2)

cv.waitKey(0)
cv.destroyAllWindows()
