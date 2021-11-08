# importing required libraries of opencv
import cv2

from matplotlib import pyplot as plt

image1 = cv2.imread('../assets/paper.png', 0)
image2 = cv2.imread('../assets/globalaihub.png', 0)
image3 = cv2.imread('../assets/paper_image.png', 0)

histogram1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([image3], [0], None, [256], [0, 256])

plt.plot(histogram3)

plt.show()
