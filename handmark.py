import cv2 as cv
import mediapipe as mp

mp_hand = mp.solutions.hands
hands = mp_hand.Hands()
mp_drawing = mp.solutions.drawing_utils

capture = cv.VideoCapture(0, cv.CAP_DSHOW)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    success, frame = capture.read()

    #Convert b/c OpenCV initially is BGR
    result = hands.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    #Checks the location of the hand
    print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, 
                                      hand_landmarks, 
                                      mp_hand.HAND_CONNECTIONS,

                                      #Change Color of Dots and Lines (1: Dots, 2: Lines)
                                      mp_drawing.DrawingSpec(color=(0, 0, 0)),
                                      mp_drawing.DrawingSpec(color=(255, 255, 255))
                                      )

    if success:
            cv.imshow("Captured Image", frame)
            if cv.waitKey(1) != -1:
                break

capture.release()
cv.destroyAllWindows()