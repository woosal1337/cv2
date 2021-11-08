import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../assets/globalaihub.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.plot(histogram, color='k')
plt.show()