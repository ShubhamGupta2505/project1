from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.geometry("3936x1728")
root.title('this ia all about images')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')
my_img = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a2.png"))
my_label = Label(image=my_img)
my_label.pack()

def trio():

    alok = Tk()
    label3 = Label(alok,text="welcome to new image")
    label3.pack()
    def quadra():
        lucky = Tk()
        label4 = Label(lucky,text="lucky is pagal and kutta")
        label4.pack()
    my_img1 = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a5.png"))
    my_label2 = Label(image=my_img1)
    Button6 = Button(alok,text="another window!",command=quadra)
    button6.pack()
    my_label2.pack(row=1,column=0)

b1 = Button(root,text="lets try new window",command=trio)
b1.pack()


button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()

root.mainloop()