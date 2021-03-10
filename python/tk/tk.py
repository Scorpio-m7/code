import hashlib
import webbrowser
import tkinter as tk
from tkinter import *

class APP():
	def __init__(self, master):
		frame2=tk.Frame(master)#用框架来将主键分开,创建一个小框
		self.hi_there=tk.Button(frame2,text="hello",fg="blue",bg="pink",command=self.say_hi)#在frame中创建按钮,字体色为蓝色,背景色为粉色,按下执行say_hi函数
		self.hi_there.pack()
		frame2.pack(side=tk.LEFT)#放在窗口最左边
		
	def say_hi(self):
		var.set("nice to meet you")#重新设置文字
		print("hi")

app=tk.Tk()#生成root窗口,实例化tk
app.title("在这里设置标题栏")
frame1=Frame(app)#使用框架调整
var=StringVar()#设置字符串变量
var.set("这里是窗口\n文字")#可以使用转义字符
theLabel=tk.Label(frame1,textvariable=var,justify=RIGHT)#属于frame1框架,可变文字,右对齐
theLabel.pack()#自动调节尺寸和位置
#*******************************************************************
photo=PhotoImage(file="1.png")#实例化图片对象,不能使用jpg文件头的图片
imgLabel=Label(frame1,image=photo,text="漂浮字体",compound=CENTER,font=("宋体",20),fg="red")#设置混合模式,文字在正上方显示,20号宋体
imgLabel.pack()
#********************************************************************
theLabel=APP(app)
frame1.pack(padx=20,pady=10)#x轴20,y轴10
#********************************************************************
v=[]
NUM=["1","2","3","4"]
for number in NUM:
	v.append(IntVar())#设置整型变量
	b=Checkbutton(app,text=number,variable=v[-1])#多选框
	b.pack(anchor=W)#左对齐
#*********************************************************************	
group=LabelFrame(app,text="最好的语言是")#创建group框架
group.pack()
LANGS=[("python",1),("perl",2),("ruby",3),("lua",4)]
w=IntVar()
for lang,num in LANGS:
	x=Radiobutton(group,text=lang,variable=w,value=num,indicatoron=False)#单选框,去掉前边的圆框
	x.pack(fill=X)#横向填充
#**********************************************************************
sb=Scrollbar(app)#创建
sb.pack(side=RIGHT,fill=Y)#滚动条靠右,沿y轴填充
theLB=Listbox(app,selectmode=EXTENDED,height=3,yscrollcommand=sb.set)#创建选项列表,开启多选模式,可显示11项,设置垂直滚动条为sb
theLB.pack(side=LEFT,fill=BOTH)
for item in range(1000):
	theLB.insert(END,item)#在最后一个位置添加

sb.config(command=theLB.yview)#移动滚动条改变显示内容
theButton=Button(app,text="删除",command=lambda x=theLB:{print(x.get(ACTIVE)),x.delete(ACTIVE)})#删除当前所选
theButton.pack()
#************************************************************************
text=Text(app,width=30,height=10,undo=True,autoseparators=False)#创建文本框,开启可撤销模式,不自动插入分隔符
text.pack()
text.insert(INSERT,"这是文字后面是链接baidu.com")#加入文字
photo2=PhotoImage(file="1.png")#创建图片
def create_image():
	text.image_create(END,image=photo2)#可以将图片放入文本框
b1=Button(text,text="出现图片",command=create_image)#创建按钮
#text.window_create(INSERT,window=b1)#可以将按钮放在文本框
#*************************************************************************
text.tag_add("tag1","1.1","1.4","1.6")#添加tag1标签,选中第一行第二个到第一行第五个前和第一行第七个
text.tag_config("tag1",background="yellow")#设置tag1标签的背景为黄色
text.tag_add("link","1.9","1.18")#添加link标签,选中第一行第8个到第一行第17个前
text.tag_config("link",underline=True)#显示link的下划线
def show_arrow_cursor(event):
	text.config(cursor="hand2")#鼠标变成手的样式
def show_xterm_cursor(event):
	text.config(cursor="xterm")#鼠标变成可输入的样式
def click(event):
	webbrowser.open("http://baidu.com")#默认浏览器打开网页
text.tag_bind("link","<Enter>",show_arrow_cursor)#绑定事件,当鼠标进入时,调用函数
text.tag_bind("link","<Leave>",show_xterm_cursor)#绑定事件,当鼠标离开时,调用函数
text.tag_bind("link","<Button-1>",click)#绑定事件,当鼠标左击时,调用函数
def callback(event):
	print(event.keysym)#打印按到的字符
	text.edit_separator()#插入分隔符
text.bind('<Key>',callback)#当键盘输入调用函数
def show():
	text.edit_undo()#撤销上一次输入
Button(app,text="撤销",command=show).pack()
#*************************************************************************
w=Spinbox(app,values=("1","2","zt"))#设置选择框
w.pack()
#*************************************************************************
def create():
	top=Toplevel()#创建窗口
	top.attributes("-alpha",0.5)#设置半透明
	top.title("窗口名称")
	msg=Message(top,text="窗口内容文字")
	msg.pack()
Button(app,text="创建窗口",command=create).pack()
app.mainloop()#窗口主事件循环,由tkinter接管程序
