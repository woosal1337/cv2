import cv2

image = cv2.imread("../assets/img.png")

x, y, w, h = 180, 65, 700, 750
cropped_image = image[y:y + h, x:x + w]

cv2.imshow("Cropped", cropped_image)
cv2.waitKey(0)
