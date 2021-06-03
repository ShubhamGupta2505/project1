from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title('hiiiiiii')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')

#showinfo ,showwarning ,showerror ,askquestion ,askokcancel ,askyesno
def popup():
    response = messagebox.askyesno("This is my Popup !!","Hello World !!")
    Label(root,text=response).pack()
    if response == 1:
        Label(root,text="You clicked Yes !",command=root.quit()).pack()
    else:
        Label(root,text="You clicked No!").pack()

Button(root,text="Popup",command=popup).pack()

root.mainloop()