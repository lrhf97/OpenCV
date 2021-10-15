import cv2, time

# first_frame = None
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(cv2.CAP_V4L2)

while True:
        
    check, frame = video.read()


    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # returns 4 points.  X and Y of top left corner and then width and height
    faces = face_cascade.detectMultiScale(gray_img,
                                            scaleFactor=1.05,
                                            minNeighbors=5)

    for x, y, w, h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Color Frame",frame)

    key = cv2.waitKey(1) 

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows