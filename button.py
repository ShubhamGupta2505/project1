from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root,text="Look I Clcked a button !!!!!!!!!!!")
    myLabel.pack()
# Creating a label Widget
myButton = Button(root,text="Click me !!!",padx=50,command=myClick,fg="blue",bg="green")
myButton.pack()

root.mainloop()