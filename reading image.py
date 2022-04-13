import cv2 as cv

img=cv.imread('C:/Users/Acer/Pictures/Capturejj.PNG')  # cv.imread(<path of the image>) to load image

cv.imshow('photo',img) # cv.imshow(<window_name>, <image to be loaded>)

cv.waitKey(0)
