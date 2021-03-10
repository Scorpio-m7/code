from tkinter import *
root=Tk()
Label(root,text="账号:").grid(row=0,column=0)#调整到0行0列
Label(root,text="密码:").grid(row=1,column=0)#调整到1行0列
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1).grid(row=0,column=1,padx=10,pady=5)#放置输入框,调整到0行1列
e2=Entry(root,textvariable=v2,show="$").grid(row=1,column=1,padx=10,pady=5)#密码用$符隐藏，调整到1行1列
def show():
	print("账户:%s" % v1.get())#输出获取的文本
	print("密码:%s" % v2.get())

photo=PhotoImage(file="1.png")#实例化图片对象,不能使用jpg文件头的图片
imgLabel=Label(root,image=photo).grid(row=0,column=3,rowspan=3)#照片放在3列占3行
Button(root,text="显示密码",width=10,command=show).grid(row=2,column=0,sticky=W,padx=10,pady=5)#宽度10的按钮,调整到2行0列,靠左
Button(root,text="退出",width=10,command=root.quit).grid(row=2,column=1,sticky=E,padx=10,pady=5)#调用自带函数qiut退出,调整到2行1列,靠右
mainloop()