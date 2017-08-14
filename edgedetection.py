import cv2
import numpy as np

stream=cv2.VideoCapture(0)



while True:
    ret, frame=stream.read()
    
    lap = cv2.Laplacian(frame,cv2.CV_64F)    
    
    sobx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5) 
    soby = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)    
    edges = cv2.Canny(frame,100,150)

    cv2.imshow('video',lap)
    #cv2.imshow('sobx',sobx)
    #cv2.imshow('soby',soby)
    #cv2.imshow('edges',edges)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break  
   
stream.release()
cv2.destroyAllWindows()