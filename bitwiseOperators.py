import cv2
import numpy as np

image1 = cv2.imread("black-white01.png")
image2 = cv2.imread("black-white02.png")

bit_AND = cv2.bitwise_and(image1, image2)
bit_OR = cv2.bitwise_or(image1, image2)
bit_XOR = cv2.bitwise_xor(image1, image2)
bit_NOT1 = cv2.bitwise_not(image1)
bit_NOT2 = cv2.bitwise_not(image2)
"""
cv2.imshow("black-white1", image1)
cv2.imshow("black-white2", image2)
"""
cv2.imshow("bit_AND", bit_AND)
cv2.imshow("bit_OR", bit_OR)
cv2.imshow("bit_XOR", bit_XOR)
cv2.imshow("bit_NOT1", bit_NOT1)
cv2.imshow("bit_NOT2", bit_NOT2)


cv2.waitKey(0)
cv2.destroyAllWindows()
