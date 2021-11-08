import cv2

image = cv2.imread("../assets/img.png")
image = cv2.resize(image, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)

text = "This is a girl image"
position = (30, 50)  # Left-Bottom
color = (0, 0, 255)  # Blue Green Red
font_size = 1
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text, position, font, font_size, color, thickness)

cv2.imshow("Text", image)
cv2.waitKey(0)
