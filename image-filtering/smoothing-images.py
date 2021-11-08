import numpy as np
import cv2

image = cv2.imread("../assets/globalaihub.png")
image = cv2.resize(image, (256, 128))

image_blur = cv2.blur(image, (5, 5))
image_gaussian = cv2.GaussianBlur(image, (5, 5), 0)
image_median = cv2.medianBlur(image, 5)
image_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

final_image = np.concatenate([image, image_blur, image_gaussian, image_median, image_bilateral], axis=0)

cv2.imshow("Final Image", final_image)
cv2.waitKey(0)