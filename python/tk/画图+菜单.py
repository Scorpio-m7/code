from tkinter import *
root=Tk()
w=Canvas(root,width=200,height=100)#创建画布
w.pack()
line1=w.create_line(0,25,200,25,fill="yellow")#创建从(0,25)到(200,25)的黄线
line2=w.create_line(100,0,100,100,fill="red",dash=(4,4))#创建从(110,0)到(100,100)的红虚线
rect1=w.create_rectangle(50,25,150,75,fill="red",dash=(4,4))#创建(50,25)到(150,75)围成的红虚线长方形
w.create_oval(50,25,150,75,fill="pink")#创建粉色椭圆
w.coords(line1,0,50,200,50)#移动至(0,50)到(200,50)
w.itemconfig(rect1,fill="blue")#修改颜色属性
Button(root,text="删除",command=(lambda x=ALL:w.delete(x))).pack
#*******************************************************************************
def callback():
	print("hi")
menubar=Menu(root)#添加菜单
filemenu=Menu(menubar,tearoff=False)#关闭菜单分离
menubar.add_cascade(label="file",menu=filemenu)#添加一级菜单
filemenu.add_command(label="open",command=callback)#下拉菜单
filemenu.add_command(label="save")
filemenu.add_separator()#添加分割线
filemenu.add_command(label="quit",command=root.quit)
editmenu=Menu(menubar)#新建菜单
menubar.add_cascade(label="edit",menu=editmenu)#添加一级菜单
editmenu.add_command(label="x")#二级菜单
editmenu.add_command(label="c")
root.config(menu=menubar)#绑定窗口
#****************************************************************************
menubar2=Menu(root)#添加菜单
menubar2.add_command(label="h",command=callback)
menubar2.add_command(label="q")
def popup(event):
	print("位置是",event.x,event.y)#越靠左上越小
	menubar2.post(event.x_root,event.y_root)#右键处展开菜单
root.bind("<Button-3>",popup)#右键触发
#*****************************************************************************
OPTIONS=["PYTHON","C","PHP"]#添加列表
variable=StringVar()#字符串变量
variable.set(OPTIONS[0])#默认值
w=OptionMenu(root,variable,*OPTIONS)#设置可选菜单按钮
w.pack()
mainloop()