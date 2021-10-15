import cv2, time

video = cv2.VideoCapture(cv2.CAP_V4L2)

while True:
        
    check, frame = video.read()

    # print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows