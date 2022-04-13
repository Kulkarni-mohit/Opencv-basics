import cv2 as cv
import numpy as np

blank=np.zeros((400,400), dtype='uint8')

rectangle=cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200), 200, 255, -1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)


# bitwise AND --> shows intersection of images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND",bitwise_and)


# Bitwise OR --> shows intersection and non intersection of images
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR",bitwise_or)


# Bitwise XOR --> shows non intersection of images
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)


# Bitwise Not
bitwise_not= cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not',bitwise_not)

bitwise_not_circle= cv.bitwise_not(circle)
cv.imshow('Bitwise Not',bitwise_not_circle)


cv.waitKey(0)
