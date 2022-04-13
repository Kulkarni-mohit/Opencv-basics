"""Histograms basically allows us to visualize the distribution of pixel intensities in an image. So its a color image or its a grayscale image, you can visualize
these pixel intensity distributions with the help of histogram, which is kind of like a graph or plot that will give a high level intuition of the pixel distriution
in the image. """

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('C:/Users/Acer/Pictures/Captureb+.png')
cv.imshow('Image',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask',mask)

# Grayscale Histogram
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Color Histogam')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
"""
plt.figure()
plt.title('Color Histogam')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask )
cv.imshow('Mask',masked)

# Color Histogram
colors=('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], mask, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)
