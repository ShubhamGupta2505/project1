from tkinter import *
root = Tk()
# Creating a label Widget
myLabel1 = Label(root, text="Hello World! ")
myLabel2 = Label(root, text="My name is Shubham Gupta ")
myLabel3 = Label(root, text="                                 ")
#Shoving it on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=10)
myLabel3.grid(row=1, column=4)

root.mainloop()