import cv2

img = cv2.imread('../assets/paper.png')
img = cv2.resize(img, (512, 512))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
img_blur = cv2.resize(img_blur, (512, 512))

sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

cv2.imshow("Original Image", img)
cv2.imshow('Sobel Output', sobelxy)
cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
