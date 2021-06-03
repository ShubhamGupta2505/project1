from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('This is my Title ......')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')
'''
r = IntVar()
r.set("2")
'''
MODES =[
    ("Pepporani","Pepporani"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]
pizza = StringVar()
pizza.set("Pepporani")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel1 = Label(root,text=value).pack()
'''

Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda :clicked(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda :clicked(r.get())).pack()
'''
mybutton = Button(root,text="Click me!",command=lambda :clicked(pizza.get())).pack()

mylabel = Label(root,text=pizza.get()).pack()


root.mainloop()