import cv2
import numpy as np

stream=cv2.VideoCapture(0)



while True:
    ret, frame=stream.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Intro to OpenCV- Video Input, Color And Video Analysis With Python',(100,130),font,1,(255,255,255),2)
    cv2.line(frame,(0,150),(1600,150),(185,128,41),10)
    cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)
    cv2.imshow('video',frame)
   
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break  
   
stream.release()
cv2.destroyAllWindows()