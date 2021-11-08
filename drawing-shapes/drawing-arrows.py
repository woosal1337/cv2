import cv2

path = "../assets/img.png"

image = cv2.imread(path)
image = cv2.resize(image, (256, 256))

image = cv2.arrowedLine(image, (int(image.shape[0] * 0.1), int(image.shape[1] * 0.1)),
                        (int(image.shape[0] * 0.9), int(image.shape[1] * 0.9)),
                        (0, 0, 255), 5)

cv2.imshow("Arrow", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
