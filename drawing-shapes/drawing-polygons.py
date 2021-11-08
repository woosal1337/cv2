import numpy as np
import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 0.25), int(image.shape[1] * 0.25)))

pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)

image = cv2.polylines(image, [pts],
                      isClosed=True, color=(0, 0, 255), thickness=5)

cv2.imshow("Reading Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
