import cv2 as cv

#This is setting the size for the Video Capture
capture = cv.VideoCapture(0, cv.CAP_DSHOW)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    success, frame = capture.read()

    if success:
        cv.imshow("Captured Image", frame)
        if cv.waitKey(1) != -1:
            break

cv.destroyAllWindows()