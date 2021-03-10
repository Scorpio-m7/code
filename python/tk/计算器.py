from tkinter import *
master=Tk()
frame=Frame(master)
frame.pack(padx=10,pady=10)
v1=StringVar()
v2=StringVar()
v3=StringVar()
def test(content):
	return content.isdigit()#如果是数字则返回

textCMD=master.register(test)#用register函数包装test函数,才能识别
e1=Entry(frame,width=10,textvariable=v1,validate="key",validatecommand=(textCMD,'%P')).grid(row=0,column=0)#validate="key"有任何输入操作都会被拦截进行检查
Label(frame,text="+").grid(row=0,column=1)
e2=Entry(frame,width=10,textvariable=v2,validate="key",validatecommand=(textCMD,'%P')).grid(row=0,column=2)#validatecommand选项会调用textCMD检查,%P表示最新内容
Label(frame,text="=").grid(row=0,column=3)
e3=Entry(frame,width=10,textvariable=v3,state="readonly").grid(row=0,column=4)#只读状态
def calc():
	result=int(v1.get())+int(v2.get())#计算结果
	v3.set(str(result))#设置结果

Button(frame,text="计算结果",command=calc).grid(row=1,column=2,pady=5)
Button(frame,text="退出",width=10,command=frame.quit).grid(row=1,column=3)
mainloop()