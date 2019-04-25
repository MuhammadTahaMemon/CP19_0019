from tkinter import *


root = Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Detection on", variable = CheckVar1, onvalue = 1, offvalue = 0, height=10, width = 50)
C1.pack()

C2 = Checkbutton(root, text = "Detection off", variable = CheckVar2,onvalue = 1, offvalue = 0, height=3, width =50)
C2.pack()

button1 = tk.Button(root, text='submit', width=30, command=root.destroy,bg="yellow",height="3")
button1.pack()

root.mainloop()