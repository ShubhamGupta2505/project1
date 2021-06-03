from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('hiiiiiii')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')
# New window created
def open():
    global my_img
    top = Toplevel()
    label = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/asd.png"))
    mylabel1 = Label(top, image=my_img).pack()
    btn2 = Button(top,text="Close Window ",command=top.destroy).pack()



btn = Button(root,text="Open Second Window",command=open).pack()
root.mainloop()