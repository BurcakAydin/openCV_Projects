import cv2 as cv
import numpy as np

image = cv.imread("kevinCostner.jpg")
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(image, kernel, iterations=1)
dilation = cv.dilate(erosion, kernel, iterations=1)
opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
gradian = cv.morphologyEx(image, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel)

"""
closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
cv.imshow("original", image)
cv.imshow("dilation", dilation)
cv.imshow("erosion", erosion)

cv.imshow("opening", opening)
cv.imshow("closing", closing)
cv.imshow("gradian", gradian)
"""
cv.imshow("tophat", tophat)
cv.imshow("blackhat", blackhat)

cv.waitKey(0)
cv.destroyAllWindows()
