import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    # works on Image,Videos, and live video
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture= cv.VideoCapture(0) # 0 for webcam, viewing some video then file location, IP webcam for mobile camera (http address/video)

while True:
    istrue, frame = capture.read() 
    resize=rescaleFrame(frame, 1)
    cv.imshow("Video", resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
