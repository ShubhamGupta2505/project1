from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('hiiiiiii')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')

frame = LabelFrame(root,text="This is my Frame",padx=5,pady=10)
frame.pack(padx=10,pady=5)

b= Button(frame,text="Do not click here ...")
b.pack()

root.mainloop()