import cv2
import numpy as py

cap = cv2.VideoCapture(0)
while(1):
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) and 0xff == ord('q'):
         break
cap.release()            
cv2.destroyAllWindows()