import numpy as np
import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (256, 256))
image_shape = image.shape

image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image2 = cv2.rotate(image, cv2.ROTATE_180)
image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

vis = np.concatenate((image1, image2, image3), axis=1)

cv2.imshow("Reading All Images:", vis)
cv2.imshow("Reading Image 1", image1)
cv2.imshow("Reading Image 2", image2)
cv2.imshow("Reading Image 3", image3)


def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, -angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


cv2.imshow("Rotated Image", rotate_image(image, 60))

cv2.waitKey(0)
cv2.destroyAllWindows()
