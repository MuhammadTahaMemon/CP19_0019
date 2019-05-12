import tkinter 
from PIL import ImageTk, Image
import cv2



root =tkinter.Tk()
root.title("Face Recognition")
root.iconbitmap(r'C:\Users\AA Computers\Desktop\New folder\user_Qpf_icon.ico')
# Create a frame
app = tkinter.Frame(root,bg='white')
app.grid()
# Create a label in the frame
lmain = tkinter.Label(app)
lmain.grid()
root.geometry("900x600")


# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 




namelabel_1=tkinter.Label(root,text="NAME :",font='times 12 bold italic')
namelabel_1.place(x=680,y=100)

entrylabel_1=tkinter.Label(root,text="")
entrylabel_1.place(x=740,y=100)

namelabel_2=tkinter.Label(root,text="NAME :",font='times 12 bold italic')
namelabel_2.place(x=70,y=550)

entryname=tkinter.Entry(root)
entryname.place(x=140,y=550)

train_button = tkinter.Button(root, text="Add",font='times 12 bold italic')
train_button.place(x=600,y=550)

buttonlabel=tkinter.Label(root,text="Recognition",font='times 12 bold italic')
buttonlabel.place(x=760,y=380)

radio_1=tkinter.Radiobutton(root,text="Yes",value=1,font='times 12 bold italic')
radio_1.place(x=750,y=400)

radio_1=tkinter.Radiobutton(root,text="No",value=2,font='times 12 bold italic')
radio_1.place(x=800,y=400)


quit = tkinter.Button(root, bg="red", text="Quit", command=root.destroy)


video_stream()
root.mainloop()