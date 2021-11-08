import cv2

cap = cv2.VideoCapture(2)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('../assets/captured_video.avi', video_cod, 30,
                               (frame_width, frame_height))

while (True):
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame, None, fx=1 / 3, fy=1 / 3, interpolation=cv2.INTER_AREA)
        cv2.imshow('frame', frame)
        video_output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    else:
        break

cap.release()
video_output.release()
cv2.destroyAllWindows()
