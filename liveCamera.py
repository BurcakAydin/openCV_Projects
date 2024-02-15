import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)  # 0 webcam, 1 usb camera, 2 video or video adress

while True:
    ret, vision = camera.read()

    cv.imshow("Burcuk", vision)
    if cv.waitKey(30) & 0xFF == ('q'):
        break
camera.release()
cv.destroyAllWindows()
