import cv2 

img = cv2.imread("C:\\Users\\Moiz Ghanchi\\Desktop\\Pictures\\rohaan.jpg",1)
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[1]/2)))    
cv2.imshow("rohaan", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()    