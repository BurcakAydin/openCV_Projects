import cv2
import numpy as np

childrenDay_image = cv2.imread("childrenDay.jpg")
slice_image = childrenDay_image[50:150, 200:300]

childrenDay_image[0:100, 0:100] = slice_image
childrenDay_image[200:250, 150:200] = (0, 150, 255)

# childrenDay_image[:, :, 0] = 255
# childrenDay_image[:, :, 1] = 0
# childrenDay_image[:, :, 2] = 255
# slice_image[:, :, 2] = 255
# cv2.imshow("Slice of Image", slice_image)
cv2.imshow("23April", childrenDay_image)

cv2.waitKey(0)  # herhangi tuşa basana kadar pencereyi görünür kıl
cv2.destroyAllWindows()  # kapattığımda tüm opencvleri kapatıyor
