import cv2,time
face=cv2.CascadeClassifier(r"C:\Users\Azhar\Documents\haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)

a=1
while True:
    a+=1
    check,frame=video.read()
    
    faces= face.detectMultiScale(frame,1.2,5)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,500,500),1)



    cv2.imshow ("capturing",frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
print(a)     
video.release()
cv2.destroyAllWindows()