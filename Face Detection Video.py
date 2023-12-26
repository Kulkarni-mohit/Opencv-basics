import cv2 as cv
import time

capture= cv.VideoCapture(0)

harr_cascade = cv.CascadeClassifier('harr_face.xml')

#faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=5)


while True:
    istrue, frame1 = capture.read()
    #time.sleep(1)
    istrue, frame2 = capture.read()
    #diff = cv.absdiff(frame1, frame2)
    gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    faces_rect1 = harr_cascade.detectMultiScale(gray1, scaleFactor=1.7, minNeighbors=5)
    faces_rect2 = harr_cascade.detectMultiScale(gray2, scaleFactor=1.7, minNeighbors=5)

    for (x,y,w,h) in faces_rect1:
        cv.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    for (x,y,w,h) in faces_rect2:
        cv.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0), thickness=2)


    cv.imshow('Detection Faces',frame1)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
