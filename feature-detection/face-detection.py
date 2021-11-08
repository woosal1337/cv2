from cv2 import cv2

face_cascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture("../assets/video.mp4")

while True:

    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)

        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.equalizeHist(image_gray)

        faces = face_cascade.detectMultiScale(image_gray)

        for (x, y, w, h) in faces:
            # Draw ellipse around the face
            center = (x + w // 2, y + h // 2)
            image = cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        cv2.imshow('Capture - Face detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cv2.destroyAllWindows()
