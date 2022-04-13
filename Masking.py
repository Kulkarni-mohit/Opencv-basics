"""
Masking essentially allow us to focus on certain parts of an image that we'd like to focus on. i.e. if you have an image of people in it, and if you're
interested in focusing on the faces of those people, you could essentially apply masking and essentially mask over the people's faces and remove all the unwanted
parts of the image.
"""

import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Acer\Pictures\Captures.PNG')
cv.imshow('Image',img)

blank= np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank,(img.shape[1]//2 ,img.shape[0]//2),100, 255, -1)
cv.imshow('Mask',mask)

masked= cv.bitwise_and(img,img, mask=mask)
cv.imshow('Masked Image',masked)

cv.waitKey(0)
