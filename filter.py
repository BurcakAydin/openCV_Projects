import cv2 as cv

image = cv.imread('c_noise.jpg')
cv.imshow("Original", image)
"""
meanFilter = cv.blur(image, (3, 3))
meanFilter2 = cv.blur(image, (5, 5))


cv.imshow("meanFilter", meanFilter)
cv.imshow("meanFilter2 5x5", meanFilter2)

medianFilter = cv.medianBlur(image, 3)
cv.imshow("medianFilter", medianFilter)

medianFilter2 = cv.medianBlur(image, 5)
cv.imshow("medianFilter2", medianFilter2)
"""
gauss = cv.GaussianBlur(image, (3, 3), 0)
cv.imshow("Gauss", gauss)
gauss2 = cv.GaussianBlur(image, (5, 5), 0)
cv.imshow("Gauss2", gauss2)

cv.waitKey(0)
cv.destroyAllWindows()
