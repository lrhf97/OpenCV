import cv2

img = cv2.imread('PXL_20210715_153217926.jpg',0)

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
print(resized_image.shape)

cv2.imshow('A and J',resized_image)
cv2.imwrite("A and J resized.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()