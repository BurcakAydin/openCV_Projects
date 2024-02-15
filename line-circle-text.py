import cv2 as cv
import numpy as np

image = np.zeros((300, 300, 3), dtype="uint8")

cv.line(image, (0, 0), (100, 100), (0, 0, 255), 3)
cv.circle(image, (100, 100), (50), (0, 255, 0), 2)
cv.putText(image, "Burcuk merhaba", (10, 100),
           cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
cv.imshow("Image", image)

cv.waitKey(0)
cv.destroyAllWindows()
