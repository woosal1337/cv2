import cv2

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (int(image.shape[0] * 0.5), int(image.shape[1] * 0.5)))
image_shape = image.shape

center_point = (int(image_shape[0] * 0.5), int(image_shape[1] * 0.5))
radius = 100
cv2.circle(image, center_point, radius, (0, 255, 0), thickness=2)

cv2.imshow("Reading Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
