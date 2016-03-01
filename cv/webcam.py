import numpy as np
import cv2

cap1 = cv2.VideoCapture(1)
cap1.set(3, 100)
cap1.set(4, 100)

cap2 = cv2.VideoCapture(3)
cap2.set(3, 100)
cap2.set(4, 100)

cap3 = cv2.VideoCapture(0)
cap3.set(3, 100)
cap3.set(4, 100)

cap4 = cv2.VideoCapture(4)
cap4.set(3, 100)
cap4.set(4, 100)

while(True):
    ret1, frame1 = cap1.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame1', gray)

    ret2, frame2 = cap2.read()
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame2', gray)

    ret3, frame3 = cap3.read()
    gray = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame3', gray)

    ret4, frame4 = cap4.read()
    gray = cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame4', gray)

# When everything done, release the capture
cap1.release()
cap2.release()
cap3.release()
cap4.release()

cv2.destroyAllWindows()
