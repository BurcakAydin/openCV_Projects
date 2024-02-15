import cv2
import numpy as np

joker_image = cv2.imread('joker.jpg')

joker_image[50, 30] = [255, 255, 255]

for i in range(368):  # uyarı geldi, 400 yazamdım, genişlik 368miş :)
    joker_image[150, i] = [255, 255, 255]

cv2.imshow("Joker", joker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
