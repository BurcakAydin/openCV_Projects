import numpy as np
import cv2
img = cv2.imread('logo.png', 0)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
