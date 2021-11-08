import numpy as np
import cv2

image = cv2.imread("../assets/img.png")
image = cv2.resize(image, (256, 256))

colors = {'red': (0, 0, 255), 'blue': (255, 0, 0), 'yellow': (0, 255, 255)}
cv2.line(image, (0, 0), (300, 300), colors['red'], 3)
cv2.rectangle(image, (0, 0), (100, 100), colors['blue'], 3)
ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300))
if ret:
    cv2.line(image, p1, p2, colors['yellow'], 3)
cv2.imshow("ClipLine", image)
cv2.waitKey(0)
cv2.destroyAl1lWindows()
