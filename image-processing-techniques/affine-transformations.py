import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = "../assets/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, (256, 256))
image_shape = image.shape

rows, cols, ch = image.shape

pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(image, M, (cols, rows))

plt.subplot(121)
plt.imshow(image)
plt.title('Input')

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
