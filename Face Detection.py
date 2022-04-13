import cv2 as cv

image = cv.imread('Face detection img.jpg')
img = cv.resize(image, (500,500))
#cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

harr_cascade = cv.CascadeClassifier('harr_face.xml')

faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.19, minNeighbors=9)

print(faces_rect)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detection Faces',img)



cv.waitKey(0)
