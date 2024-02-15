import cv2
import numpy as np

kemalSunal = cv2.imread("kemalSunal.jpg")
kemalSunal[150:230, 230:370, 0] = 255
kemalSunal[150:230, 230:370, 1] = 200
# kemalSunal[:, :, 0] = 50  # 1 koyarsam yeşil, 2 koyarsam kırmızı olur
# kemalSunal[:, :, 1] = 200
# kemalSunal[:, :, 2] = 250 Kırmızıyı hiç kullanmadım
cv2.imshow("Kemal Sunal", kemalSunal)

cv2.waitKey(0)
cv2.destroyAllWindows()
