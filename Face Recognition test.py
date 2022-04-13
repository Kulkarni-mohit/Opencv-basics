import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('harr_face.xml')

people=[]
for i in os.listdir(r'C:\Users\Acer\Pictures\Face Detection'):
    people.append(i)


features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Acer\Pictures\Testset\107.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the Face in the Image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Person', img)

cv.waitKey(0)
