import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    # works on Image,Videos, and live video
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width,height):
    # works only for Live video (from webcam
    capture.set(3,width)
    capture.set(4,height)

img=cv.imread('C:/Users/Acer/Downloads/Lap 1.jpg')

img_resized=rescaleFrame(img,scale=0.5)

cv.imshow('image',img)
cv.imshow('img_resized',img_resized)

cv.waitKey(0)
