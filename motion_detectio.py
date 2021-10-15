import cv2, time

first_frame = None

video = cv2.VideoCapture(cv2.CAP_V4L2)

while True:
        
    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray_frame)

    #threshold to split it up and down based on an "amount different".  In this case '30
    thresh_frame=cv2.threshold(delta_frame, 35, 255, cv2.THRESH_BINARY)[1]

    #dilate blends together some of the bright spots that are close together
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # filter out smaller items. if the countour has less than 1000 pix then move on to the next one.
    for contour in cnts:
        if cv2.contourArea(contour) <1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow("Gray Frame",gray_frame)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Framqe",frame)



    key = cv2.waitKey(1) 

    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows