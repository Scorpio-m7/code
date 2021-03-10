from tkinter import *
root=Tk()
w=Canvas(root,width=800,height=600)#创建画板
w.pack()
def paint(event):
    x1,y1=(event.x-1),(event.y-1)#event表示触发的位置
    x2,y2=(event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2)#创建椭圆
def m(event):
    print("当前位置是",event.x,event.y)
w.bind("<B1-Motion>",paint)#按住左键调用函数
w.bind("<Motion>",m)#鼠标移动调用函数
Label(root,text="按住左键开始").pack()
mainloop()