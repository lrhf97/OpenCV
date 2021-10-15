import cv2



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('photo.jpg')
# img = cv2.imread('PXL_20210715_153217926.jpg')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# returns 4 points.  X and Y of top left corner and then width and height
faces = face_cascade.detectMultiScale(gray_img,
                                        scaleFactor=1.1,
                                        minNeighbors=5)

# take those 4 poits and make a rectangle
for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)
# resized_image = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))


cv2.imshow("gray image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 