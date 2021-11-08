import numpy as np
import cv2

image = cv2.imread("../assets/img.png")

common_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
common_sharpen = cv2.filter2D(image, -1, common_filter)

mexican_hat_filter = np.array(
    [[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])
mexican_hat_sharpen = cv2.filter2D(image, -1, mexican_hat_filter)

custom_filter = np.array([[3, -2, -3], [-4, 8, -6], [5, -1, -0]])
custom_sharpen = cv2.filter2D(image, -1, custom_filter)

images = [image, common_sharpen, mexican_hat_sharpen, custom_sharpen]

for i in range(len(images)):
    image = images[i]
    image = cv2.resize(image, (image.shape[0] // 4, image.shape[1] // 4))
    images[i] = image

image_all = np.concatenate(images, axis=1)
cv2.putText(image_all, "ORIGINAL", (75, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(image_all, "COMMON", (340, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(image_all, "MEXICAN HAT", (590, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(image_all, "CUSTOM", (850, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow("All", image_all)
cv2.waitKey(0)