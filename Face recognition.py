import cv2 as cv
import os
import numpy as np

people=[]
for i in os.listdir(r'C:\Users\Acer\Pictures\Face Detection'):
    people.append(i)

print(people)


harr_cascade = cv.CascadeClassifier('harr_face.xml')

DIR = r'C:\Users\Acer\Pictures\Face Detection'

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join( path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = harr_cascade.detectMultiScale(gray, 1.5, 10)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list an labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


