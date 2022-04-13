""" Thresholding is a binary realisation of an image. In general, we want to take an image and convert it to a binary image that is an image where pixels are either
zero(black), or 255 (white). A very simple example of thresholding would be to take an image and take some particular value that we're going to call the thresholding
value. And compare each pixel of the image to this theshold of value. If that pixel intensity is less than the threshold value, we set that pixel intensity to zero.
And if it is above this threshold value, we set it to 255, or white, So in this sense we can essentially create a binary image just from a regular standlone image. """

import cv2 as cv

img = cv.imread(r'C:\Users\Acer\Pictures\York.jpg')
cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adoptive Thresholding
""" In Simple Thresholding we need to manually specify a specific threshold but in Adoptive tresholding computer find the optimal threshold value by itself."""

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)




cv.waitKey(0)
