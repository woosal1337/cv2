import cv2
import numpy as np

image_path = "../assets/paper_image.png"

image = cv2.imread(image_path)
image_shape = image.shape

pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (500, 600))

cv2.imshow('frame', image)
cv2.imshow('frame1', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
