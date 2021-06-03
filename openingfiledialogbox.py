from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title('hiiiiiii')
root.iconbitmap('c:/Users/gf/Downloads/abc.ico')

root.filename = filedialog.askopenfilename(initialdir="c:/Users/gf/Downloads",title="SElect a File  :",filetypes=(("png file ","*.png"),("jpg files","*.jpg")))


root.mainloop()