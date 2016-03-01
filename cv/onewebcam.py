import numpy as np
import cv2

cap1 = cv2.VideoCapture(1)
cap1.set(3, 1000)
cap1.set(4, 1000)

while(True):
    ret1, frame1 = cap1.read()
    cv2.imshow('frame1', frame1)

# When everything done, release the capture
cap1.release()

cv2.destroyAllWindows()
