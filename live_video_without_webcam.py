import cv2
while True:
    video_capture = cv2.VideoCapture("http://192.168.1.100:8080//shot.jpg")


    check, img = video_capture.read()
    cv2.imshow("FaceDetection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()