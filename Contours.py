import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Acer\Pictures\Captures.PNG')
cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)   # Contours in simple language is the outline of image stored in list
print(f'{len(contours)} contour(s) found!')
"""
# Another Way
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)      # It binarize the img as colors below 125 will be black and above 125 to 255 will be white
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # Contours in simple language is the outline of image in list
print(f'{len(contours)} contour(s) found!')
"""

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
