from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('This is my image viewer')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')
#here we need to write the address of photos in the computer inside""  address  "

my_img1 = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/asd.png"))
my_img2  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a1.png"))
my_img3  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a2.png"))
#my_img4  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a3.png"))
my_img5  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a4.png"))
my_img6  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a5.png"))
#my_img7  = ImageTk.PhotoImage(Image.open("c:/Users/gf/Downloads/a6.png"))

image_list = [my_img1,my_img2,my_img3,my_img5,my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root,text=">>",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)








button_back = Button(root,text="<<",command=back,state=DISABLED)
button_exit = Button(root,text="Exit this window",command=root.quit)
button_forward = Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()