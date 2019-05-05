import cv2

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def dataset(img,userID,imageID):
    cv2.imwrite("data1/user."+str(userID)+"."+str(imageID)+".jpg",img)
    
def detect(img,faceCascade):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    features=faceCascade.detectMultiScale(gray_img,1.2,10)
    coords=[]
    for (x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
        coords=[x,y,w,h]
    if len(coords)==4:
        rimg=img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
    dataset(rimg,userID,imgID)    
    return img
video=cv2.VideoCapture(0)
userID=1
imgID=0
while True:
    
    check,img=video.read()
    
    img=detect(img,faceCascade)
    
    cv2.imshow("azhar",img)
    imgID+=1
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cv2.destroyAllWindows()        
