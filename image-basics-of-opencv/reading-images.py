import cv2

image_path = "../assets/img.png"
image = cv2.imread(image_path)

cv2.imshow("Reading Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
