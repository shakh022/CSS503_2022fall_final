import cv2
faceCascade = cv2.CascadeClassifier('Final\haarcascade_frontalface_default.xml')

# colorImage = cv2.imread("Final\photo.jpg")
# colorImageGray = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(colorImageGray, 1.1, 4)
# #identification rectangle
# for (x,y,w,h) in faces:
#     cv2.rectangle(colorImage, (x,y), (x+w, y+h), (255,0,0),2)

# cv2.imshow('detected face:',colorImage)
# cv2.waitKey()

videoCapture = cv2.VideoCapture(0)
while True:
    _, img = videoCapture.read()
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imageGray, 1.05, 4)

    #identification rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    cv2.imshow('detected face:',img)
    k= cv2.waitKey(30) & 0xff
    if k==27:
        break
videoCapture.release()


