
from tkinter import *
from tkinter import messagebox


window = Tk()
 
window.title("Taha's")
 
lbl = Label(window, text="Hello World")
lbl = Label(window, text="Hello", font=("Calibri", 50))
lbl.grid(column=2, row=0)
window.geometry('1000x600')

txt = Entry(window,width=30)
txt.grid(column=2, row=2)
txt.focus()
def clicked():
    
    res = messagebox.askyesno('Confirmation','Are You Sure With This Data?')
    messagebox.showinfo('Data Inserted', 'Successfully Inserted Data')
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
    lbl.grid(column=3, row=0)


rad1 = Radiobutton(window,text='Male', value=1)
 
rad2 = Radiobutton(window,text='Female', value=2)
 
rad3 = Radiobutton(window,text='Other', value=3)
 
rad1.grid(column=1, row=4)
 
rad2.grid(column=2, row=4)
 
rad3.grid(column=3, row=4)

btn = Button(window, text="Click", fg="white", bg="lightblue", command=clicked)

btn.grid(column=2, row=3)



window.mainloop()