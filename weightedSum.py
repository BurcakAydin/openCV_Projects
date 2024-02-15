import cv2
import numpy as np


image1 = cv2.imread('emelSayin.jpg')
image2 = cv2.imread('turkanSoray.jpg')

print(image1[150, 200])
print(image2[300, 430])

cv2.imshow('Emel Sayın', image1)
cv2.imshow('Türkan Şoray', image2)

print(image1[200, 200] + image2[300, 430])
cv2.waitKey(0)
cv2.destroyAllWindows()
