from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
root=Tk()
def callback():
    fileName=filedialog.askopenfilename(defaultextension=".png",filetypes=[("PNG",".png"),("JPG",".jpg")])#打开文件，默认后缀png,文件类型png或jpg
    print(fileName)
def callback2():
    filename=colorchooser.askcolor()#颜色选择
    print(filename)
Button(root,text="打开文件",command=callback).pack()
Button(root,text="选择颜色",command=callback2).pack()
mainloop()