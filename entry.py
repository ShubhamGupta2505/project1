from tkinter import *
root = Tk()
e = Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"Enter your name : ")

def myClick():
    myLabel = Label(root,text="Hello" + e.get())
    myLabel.pack()
# Creating a label Widget
myButton = Button(root,text="Enter your name ",padx=50,command=myClick,fg="blue",bg="green")
myButton.pack()

root.mainloop()