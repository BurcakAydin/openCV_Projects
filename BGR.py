import cv2
import numpy as np

wolf_image = cv2.imread('wolf.jpg')  # , 0 yazarsam foto gri oluyor

cv2.imshow("Wolf", wolf_image)

print(wolf_image[(230, 80)])

print("Image Size: " + str(wolf_image.size))
print("Image Features: " + str(wolf_image.shape))
print("Image Data Type: " + str(wolf_image.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
