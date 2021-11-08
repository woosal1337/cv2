import cv2

image_path = "../assets/img.png"
image = cv2.imread(image_path)

# Converting the image to gray scale
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("../assets/new_image.png", new_image)
