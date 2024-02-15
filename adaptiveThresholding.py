import cv2

# 0 gri tonlar için, 0 yazmazsak hata veriyor
image = cv2.imread("wolf.jpg", 0)

ret, thresh1 = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)


adaptive1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 11, 2)

adaptive2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)


cv2.imshow("original", image)
cv2.imshow("simple threshold", thresh1)
cv2.imshow("adaptive1", adaptive1)
cv2.imshow("adaptive2", adaptive2)


cv2.waitKey(0)
cv2.destroyAllWindows()
