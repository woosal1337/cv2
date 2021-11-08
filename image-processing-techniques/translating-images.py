import numpy as np
import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 0.25), int(image.shape[1] * 0.25)))
image_shape = image.shape

T = np.float32([[1, 0, image_shape[1] / 3], [0, 1, image_shape[0] / 3]])

image = cv2.warpAffine(image, T, (image_shape[0], image_shape[1]))

cv2.imshow("Reading Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
