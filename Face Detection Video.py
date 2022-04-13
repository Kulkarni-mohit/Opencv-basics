import cv2 as cv

capture= cv.VideoCapture(0)

harr_cascade = cv.CascadeClassifier('harr_face.xml')

#faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=5)


while True:
    istrue, frame = capture.read() 
    resize=cv.resize(frame, (500,500))
    gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
    faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detection Faces',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
