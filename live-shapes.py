import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    ret, vision = camera.read()

    cv.rectangle(vision, (100, 100), (200, 200), (0, 0, 255), 2)
    cv.line(vision, (0, 0), (100, 100), (0, 0, 255), 3)
    cv.circle(vision, (100, 100), 50, (0, 0, 255), 5)
    cv.putText(vision, "Burcuk", (200, 200),
               cv.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 1)

    cv.imshow("Burcuk", vision)

    if cv.waitKey(25) & 0xFF == ('q'):
        break

camera.release()

cv.destroyAllWindows()
