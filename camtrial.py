import numpy as np
import cv2

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while True:
    # capture frame by frame 
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()

    if(ret0):
        cv2.imshow('Cam 0', frame0)
    
    if(ret1):
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cap1.release()
cv2.destroyAllWindows()