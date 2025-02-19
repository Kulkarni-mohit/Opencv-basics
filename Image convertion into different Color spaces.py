import cv2 as cv

img=cv.imread(r'C:\Users\Acer\Pictures\York.jpg')
cv.imshow('Image',img)

# BGR to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# BGR to HSV
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)


# BGR to L*a*b
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


# BGR to RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


# HSV to BGR
hsv_bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR',hsv_bgr)




cv.waitKey(0)
