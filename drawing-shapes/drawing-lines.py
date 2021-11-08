import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 0.5), int(image.shape[1] * 0.5)))
image_shape = image.shape

point1 = (int(image_shape[0] * 0.1), int(image_shape[1] * 0.1))
point2 = (int(image_shape[0] * 0.9), int(image_shape[1] * 0.9))
cv2.line(image, point1, point2, (0, 255, 0), thickness=2)

cv2.imshow("Reading Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
