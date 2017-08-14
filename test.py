import cv2

img = cv2.imread('tr.jpg',cv2.IMREAD_COLOR)


#lap = cv2.Laplacian(img,cv2.CV_64F)    
    
#sobx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) 
#soby = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)    
edges = cv2.Canny(img,150,200)

#cv2.imshow('video',lap)
#cv2.imshow('sobx',sobx)
#cv2.imshow('soby',soby)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()