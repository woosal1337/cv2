from cv2 import cv2

# Load the eye cascade
eyes_cascade_path = "../haarcascades/haarcascade_eye.xml"

# Load the face cascade
eyes_cascade = cv2.CascadeClassifier(eyes_cascade_path)
face_cascade_path = "../haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)

image_path = r"../assets/img.png"
image = cv2.imread(image_path)
image = cv2.resize(image, (512, 512))

# Convert image to gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.equalizeHist(image_gray)

# Detect faces in the image
faces = face_cascade.detectMultiScale(image_gray)

# Draw ellipse for each face in the image
for (x, y, w, h) in faces:
    # Draw ellipse around the face
    center = (x + w // 2, y + h // 2)
    image = cv2.ellipse(image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

    # Crop face from the image and use it for eye detection
    faceROI = image_gray[y:y + h // 2, x:x + w]

    # Detect eyes for each face
    eyes = eyes_cascade.detectMultiScale(faceROI)
    for (x2, y2, w2, h2) in eyes:
        eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
        radius = int(round((w2 + h2) * 0.25))
        # Draw circle around the eye
        frame = cv2.circle(image, eye_center, radius, (255, 0, 0), 4)

cv2.imshow('Capture - Face detection', image)
cv2.waitKey(0)
