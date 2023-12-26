import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')    # creating a blank image, dtype=uint8 is basically image

"""
#1. Paint the image with certain color
blank[:]=0,255,0           # we can use different colors with rule BGR, blank[:] means all pixels
cv.imshow("green",blank)

#for certain range of pixels
blank[200:300,300:400]=0,0,255
cv.imshow('red',blank)
"""

"""
# 2. Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=2)  # to fill whole rectangle put thickness=-1 ; Parameters : (img, initial coordinate, final coord, color,thickness)
cv.imshow('Rectangle',blank)
"""

"""
#3. Draw a circle
cv.circle(blank,(250,250),40,(0,0,255), thickness=3)
cv.imshow('circle',blank)
"""

"""
#4. Draw a line
cv.line(blank,(0,0),(250,250),(255,255,255), thickness=2)
cv.imshow('line',blank)
"""

"""
#5. Write text
cv.putText(blank,'Hello World', (150,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
"""


cv.waitKey(0)
