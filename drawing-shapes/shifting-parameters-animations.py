import cv2
import numpy as np
import time
import random

import numpy as np
import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 0.25), int(image.shape[1] * 0.25)))

x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6 = 25, 25, 110, 200, 200, 110, 70, 160, 200, 160, 70, 20
colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (122, 59, 199), (222, 222, 222), (254, 90, 199)]

for i in range(100):
    color = random.choice(colors)

    x1 += 4
    x2 += 4
    x3 += 4
    x4 += 4
    x5 += 4
    x6 += 4

    y1 -= 4
    y2 -= 4
    y3 -= 4
    y4 += 4
    y5 += 4
    y6 += 4

    pts = np.array([[x1, y1], [x2, y2],
                    [x3, y3], [x4, y4],
                    [x5, y5], [x6, y6]],
                   np.int32)

    image = cv2.polylines(image, [pts],
                          isClosed=True, color=color, thickness=2)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

    cv2.imshow("Reading Image", image)

    cv2.waitKey(50)
