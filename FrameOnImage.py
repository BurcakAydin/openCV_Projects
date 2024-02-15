import cv2
import numpy as np

image = cv2.imread('hababam.jpg')
#image[70:120, 230:290, 0] = 255
cv2.rectangle(image, (160, 160), (260, 260), [0, 0, 255], 3)
cv2.imshow('Hababam', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
