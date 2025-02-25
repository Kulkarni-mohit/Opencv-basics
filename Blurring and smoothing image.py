import cv2 as cv

img = cv.imread(r'C:\Users\Acer\Pictures\York.jpg')
cv.imshow('Image', img)


# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average Blur', average)


# Gaussian Blur
gauss= cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)


# Median Blur
median= cv.medianBlur(img,3)
cv.imshow('Median blur', median)


# Bilateral
bilateral= cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)




cv.waitKey(0)
