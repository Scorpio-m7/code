*********************************
def d(price,rate):
	final=price*rate
	#print(old)
	#old是全局变量
	old=50
	print("old",old)
	return final

old=float(input('original cost'))
rate=float(input('discount'))
#这里的rate与d函数中的变量只是名字相同
new=d(old,rate)
print(new)
*********************************
c=5
def m():
	#global c
	#global使c变量成为全局变量
	c=10
	print(c)

m()
print(c)
**********************************
def fun1():
	print('fun1正在被调用...')
	def fun2():
		print('fun2正在被调用...')

	fun2()

fun1()
#fun2()无法调用
**********************************
def fun1(x):
	def fun2(y):
		return x*y
	return fun2

i=fun1(8)
tpye(i)#发现i是一个函数类型
i(5)#返回40
fun1(8)(5)#返回40
***********************************
def fun0():
	x=5#x相当于fun00的全局变量
	def fun00():
		#解决方法
		#nonlocal x
		x*=x#这里的x只是与fun0中定义的x名字相同
		return x
	return fun00

fun0()
************************************
def add(x,y):
	return 2*x+y

add(5,1)
add=lambda x,y:2*x+y#和上面定义的函数相同
add(5,1)
************************************
list(filter(lambda x:x%2,range(10)))
#filter的第一个参数如果是函数，将第二个可迭代数据的每一个元素作为函数的参数进行计算，把返回ture的值筛选出来并成一个列表
************************************
list(map(lambda x:x*2,range(10)))#range(10)是从0到9
#将序列的每一个元素做为函数的参数进行运算，直到可迭代序列的每一个元素都加工完毕，返回所有加工后的元素，组成新序列
*************************************
def jc(x):
	for i in range(1,x):
		x*=i
	return x
	
n=int(input('输入数字'))
r=jc(n)
print("{}的阶乘是{}".format(n,r))
**************************************
def jc(x):#递归实现阶乘
	if x==1:
		return x
	else:
		return x*jc(x-1)
n=int(input('输入数字'))
r=jc(n)
print("%d的阶乘是%d" % (n,r))
**************************************
def fab(n):#迭代实现斐波那契数列
	n1,n2,n3=1,1,1#特点是速度快
	if n<1:
		print('wrong!')
		return -1
	while (n-2)>0:
		n3=n2+n1
		n1=n2
		n2=n3
		n-=1
	return n3
t=int(input('give me number'))
final=fab(t)
if final !=-1:
	print('total is %d' % final)
*************************************
def fab(n):#递归实现斐波那契数列
	if n<1:#分治思想
		print('wrong!')#速度慢
		return -1
	if n==1 or n==2:
		return 1
	else:
		return fab(n-1)+fab(n-2)

t=int(input('give me number'))
final=fab(t)
if final !=-1:
	print('total is %d' % final)
*************************************
def hanoi(n,x,y,z):#汉诺塔（从左数x，y，z柱子）
	if n==1:
		print(x,'-->',z)
	else:
		hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
		print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上
		hanoi(n-1,y,z,x)#将y上的n-1个盘子移动到z上

n=int(input('输入层数'))
hanoi(n,'X','Y','Z')
*************************************
b=['1','2','3','a','b']
s=['one','two','three']
print(b[:2],b[-2],b[1:5:2],b[::-1])#b[:2]输出从0到1的元素，范围是左闭右开,b[-2]取倒数第1个，b[1:5:2]从0到4 每隔2个选取第一个，b[::-1]反向输出列表
print('第三个是',s[b.index('3')])#index（指定索引的字符串，开始查找位置，结束位置）
*************************************
d={1:'one',2:'two',3:'three'}#冒号隔开，1代表key，one代表值
print('第三个是',d[3])
d2=dict(i='one',y='two')#这样定义的i会自动添加上''
print(d2['i'])
d2['i']='newi'
d2['t']='addt'
print(d2['i'],d2)
d3=dict((('F',70),('i',105),('s',115),('h',104)))
print(d3['h'])
**************************************
dict.fromkeys((1,2,3),'number')
dict.fromkeys((1,3),'数字')#不能修改上面的表，会重新创建一个新的字典
dict=dict.fromkeys(range(15),'yes')
for eachkey in dict.keys():
	print(eachkey)#for eachvalue in dict.value():print(eachvalue)
for eachitem in dict.items():
	print(eachitem)
print(dict.get(15,'没有这个关键字'))
14 in dict
dict.pop(3)
*************************************
a={'a':'a'}
b=a#b的地址和a相同
c=a.copy()#c的地址和a不同，所以a删除不会影响c
a.clear()#a和b的字典都会被清空
c.setdeault(5,'five')#加入关键字
d={'5','五'}
c.update(d)#替换c中5的值，使用d字典添加
*************************************
n={1,2,2}#创建集合n
s1=set([1,1,2])#创建集合s1，将重复的删除
n1={1,5,9,6,3,3,3,5,5}
n2=list(set(n1))
print(n,s1,n2)
n1.add(2)#添加元素6
n1.remove(5)#删除元素5
n3=frozenset([1,3,6,9])#冻结集合，无法添加删除
print(n1,n3)
**************************************
f=open('D:\\CTF\\web\\1.php','a+')#打开文件，可读写模式
f.write('#')#写入#，返回写入的字符数
f.readline()#读取一行
f.seek(0,0)#书签重置
for each_line in f:
	print(each_line)

f.close()#保存文件
**************************************
import os#导入os模块
os.getcwd()#返回当前工作目录
os.listdir()#列举目录文件
os.makedirs()#递归创建目录
os.remove()#删除文件
os.removedirs()#删除目录
os.system('cmd')#运行系统的shell命令
os.listdir(os.curdir)#os.curdir指当前目录
os.path.basename('D:\\python\\2.py')#去掉目录路径
os.path.dirname('D:\\python\\2.py')#去掉目录路径
os.path.join('D:\\','A','B','C')#将各个部分组合成一个路径名
os.path.split('D:\\python\\2.py')#分割文件名与路径
os.path.splitext('D:\\python\\2.py')#分割文件名与扩展名
***************************************
import pickle
mylist=[123,3.14,'abc',['list']]
with open('list.pkl','wb') as file:#以二进制形式存储数据
	pickle.dump(mylist,file)#把列表存入
file=open('list.pkl','rb')
mylist2=pickle.load(file)
print(mylist2)
****************************************
try:
	f=open('wenjian.txt','w')
	sum=1+'1'
except OSError as e:
	print('错误\n原因'+str(e))
except TypeError as e:
	print('错误\n原因'+str(e))
finally:
	f.close()#无论如何都会执行
#报出错误：raise ZeroDivisionError('除数为零')
else:#和finally语句不能同时使用
	print('没有错误')#如果try语句中的内容没有错误，则执行else语句
*****************************************
def showmaxfactor(num):
	count=num//2
	while count>1:
		if num%count==0:
			print('%d最大约数是%d' % (num,count))
			break#如果中途break跳出了，else的语句不会执行
		count-=1
		else:
			print('%d是素数' %num)
num=int(input('输入数字'))
showmaxfactor(num)
******************************************
import easygui as g
import sys
while 1:
	g.msgbox('hello world')
	msg="想学什么"
	title="互动"
	choices=["恋爱","编程","1234","书画"]
	choice=g.choicebox(msg,title,choices)
	g.msgbox("你的选择是"+str(choice),"结果")
	msg="重新开始"
	title="请选择"
	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)
******************************************
class Turtle:#类名以大写开头
	#属性
	color='green'
	legs=4
	#方法
	def eat(self):
		print("吃")
	def climb(self):
		print("爬")

tt=Turtle()
tt.climb()
class Mylist(list):#继承list的所有功能
	pass

list2=Mylist()#实例化
list2.append(5)
class A:
	def fun(self):
		print("A")

class B:
	def fun(self):
		print("B")

a=A()
b=B()
a.fun()#多态
b.fun()#不同对象对同一方法响应不同的行动
********************************************
class Ball:
	def __init__(self, name):
		self.name = name
	def kick(self):
		print("%s"%self.name)

a=Ball('球')#实例化的同时赋值
a.kick()
class Person:
	__name="zt"#私有变量：在前面加上两个_
	def getname(self):
		return self.__name

p=Person()
p.__name#私有变量无法在外部访问
p.getname()#通过内部函数访问
p._Person__name#通过特殊方法访问
***********************************************
import random as r
class Fish:
	def __init__(self):
		self.x=r.randint(0,100)
		self.y=r.randint(0,100)

	def move(self):
		self.x-=1
		self.y-=1
		print("我在",self.x,self.y)

class Goldfish(Fish):#子类Goldfish继承父类Fish
	def look(self):
		print("看我")

class Shark(Fish):
	def __init__(self):#子类重写父类的方法就会覆盖父类的方法
		super().__init__()#super函数不用给父类的名字，自动找出基类（父类）方法
		self.hungry=1

	def eat(self):
		if self.hungry:
			print("吃吃吃")
			self.hungry=0
		else:
			print("吃饱了")

class Carp(Goldfish,Shark):#多重继承
	pass

f=Fish()
f.move()
g=Goldfish()
g.move()
s=Shark()
s.eat()
s.move()
c=Carp()#多重继承可以同时继承多个父类
c.look()
c.eat()
issubclass(Goldfish,Fish)#如果Goldfish是Fish的子类则返回ture
issubclass(Fish,object)#所有类都是object的子类
isinstance(f,Fish)#如果f是Fish的实例化对象返回ture
isinstance(g,(Fish,Goldfish))#因为Goldfish是FIsh的子类，所以g也是Fish的实例化对象
****************************************************
class Turtle():#组合
	def __init__(self, x):#实例化时自动调用构造函数
		self.num = x#定义变量self.num赋值x

class Fish:
	def __init__(self, x):
		self.num = x

class Pool:
	def __init__(self,x,y):
		self.turtle=Turtle(x)#实例化
		self.fish = Fish(y)

	def print_num(self):
		print("水池共有%d只乌龟，%d只小鱼 " % (self.turtle.num,self.fish.num))#调用实例化对象

pool=Pool(1,10)
pool.print_num()
***************************************************
class C():
	def __init__(self, size=10):
		self.size =size
	def getSize(self):
		return self.size
	def setSzie(value):
		self.size=value
	def delSize(self):
		del self.size
	x=property(getSize,setSzie,delSize)

c1=C()
hasattr(c1,'size')#如果对象c有属性x则返回ture
getattr(c1,'y',"访问的属性不存在")#返回属性y的值，如果不存在打印后面的参数
setattr(c1,'y','添加属性y')#设置y属性的值，如果不存在y属性则新建y属性
delattr(c1,'y')#删除对象中的属性
c1.x#相当于c1.getSize(),好处在于可以直接调用c1的x属性直接实现三个函数
c1.x=18#相当于c1.setSize()
del c1.x#相当于c1.delSize()
***************************************************
class Rectangle:#计算长方形
	def __init__(self, x,y):#__init__函数相当于构造函数,自动执行
		self.x = x
		self.y=y
		#return "abc"#__init__函数不能有返回值
		print("我是__init__方法")
	def getPeri(self):
		return (self.x+self.y)*2
	def getArea(self):
		return self.x*self.y
	def __del__(self):#__del__在内存中释放rect类自动调用
		print("我是__del__方法")

rect=Rectangle(3,4)
rect.getPeri()
rect.getArea()
del rect
******************************************************
class New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

a=New_int('3')
b=New_int(4)
a+b
******************************************************
class Nint(int):
	def __rsub__(self, other):#这里传入的self=a，other=3
		return int.__sub__(self,other)#因为self在前，所以返回a-3

a=Nint(5)
3-a#因为3没有sub方法，所以找a的rsub方法
******************************************************
class Capstr(str):#转换成大写，继承于string
	def __new__(cls, string):#对象实例化调用的第一个方法
		string=string.upper()#因为string不可修改，所以要在实例化之前修改
		return str.__new__(cls,string)
		
a=Capstr("abcDEFg")
*******************************************************
class C:
	"""docstring for C"""
	def __getattribute__(self, name):#当该类的属性被访问时
		print("getattribute")
		return super().__getattribute__(name)

	def __getattr__(self,name):#当用户获取一个不存在的属性时
		print("getattr")

	def __setattr__(self,name,value):#当一个属性被设置时
		print("setattr")
		super().__setattr__(name,value)

	def __delattr__(self,name):#当属性被删除时
		print("delattr")
		super().__delattr__(name)

c=C()
c.x
c.x=1
del c.x
*******************************************************
class Rectangle:#计算长方形,如果是正方形只接收一个值，计算面积
	def __init__(self,width=0,height=0):
		self.width=width
		self.height=height
	def __setattr__(self,name,value):#square属性被设置时执行
		if name=='square':
			self.width=value
			self.height=value
		else:
			super().__setattr__(name,value)#调用基类（父类）的__setattr__方法，默认继承object类
	def getArea(self):
		return self.width*self.height

r1=Rectangle(5,4)
r1.getArea()
r1.square=10
r1.width
r1.getArea()
*******************************************************
class MyProperty:
	"""docstring for MyProperty"""
	def __init__(self, fget=None,fset=None,fdel=None):
		self.fget=fget
		self.fset=fset
		self.fdel=fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):#
		self.fset(instance,value)
	def __del__(self,instance):
		self.fdel(instance)
		

class C:
	"""docstring for C"""
	def __init__(self):
		self._x=None

	def getX(self):
		return self._x
	def setX(self,value):
		self._x=value
	def delX(self):
		del self._x
	x=MyProperty(getX,setX,delX)#这里把C类定义的函数传给MyProperty类，这样就可以访问C类函数的私有_x属性


c=C()
c.x='xman'
c._x
*******************************************************
class Celsius:#华氏温度和摄氏温度转换
	"""docstring for Celsius"""
	def __init__(self,value=26.0):
		self.value= float(value)
	def __get__(self,instance,owner):
		return self.value
	def __set__(self,instance,value):
		self.value=float(value)


class Fahrenheit:
	"""docstring for Fahrenheit"""
	def __get__(self, instance,owner):
		return instance.cel*1.8+32
	def __set__(self,instance,value):
		instance.cel=(float(value)-32)/1.8


class Temperature:
	"""docstring for Temperature"""
	cel=Celsius()
	fah=Fahrenheit()
		

temp=Temperature()
temp.cel
temp.cel=30
temp.fah
*******************************************************
class CountList:#定义新容器，记录列表中每个元素访问的次数
	"""docstring for CountList"""
	def __init__(self, *args):#可变数量参数
		self.value=[x for x in args]#以列表形式存入value
		self.count ={}.fromkeys(range(len(self.value)),0)#访问次数保存在字典里

	def __len__(self):
		return len(self.values)

	def __getitem__(self,key):
		self.count[key]+=1#访问一次key+1
		return self.value[key]

c1=CountList(1,3,5,9)
c2=CountList(2,4,8)
c1[1]
c2[2]+c1[1]
c1.count
*******************************************************
class Fibs:#迭代输出斐波那契数列
	"""docstring for Fibs"""
	def __init__(self,n=10):
		self.a=0
		self.b=1
		self.n=n
	def __iter__(self):#迭代器魔法方法 
		return self
	def __next__(self):#获得下一个元素，决定迭代规则
		self.a,self.b=self.b,self.a+self.b#先将b的值赋给a，然后把a+b的值赋给b
		"""
		c=self.b
		self.b=self.a+self.b
		self.a=c
		"""
		if self.a>self.n:
			raise StopIteration#结束迭代
		return self.a

fibs=Fibs(100)
for each in fibs:
	print(each)
*******************************************************
def mygen():#生成器是特殊的迭代器
	print("生成器")
	yield 1#返回值并在这里暂停
	yield 2

myg=mygen()
next(myg)
next(myg)
a=[i for i in range(100) if not(i%2) and i % 3]#把100以内可以整除2不可以整除3的数放到a
b={i:i%2==0 for i in range(10)}#10以内是否可以整除2
def libs():#生成器实现斐波那契
	a=0
	b=1
	while 1:
		a,b=b,a+b
		yield a#返回a并暂停

for each in libs():
	if each>100:#100以内的斐波那契
		break
	print(each,end=' ')

e=(i for i in range(10) if i % 2)#可以用元组表示生成器
for each in e:
	print(each)

sum(i for i in range(10) if i % 2)#10以内奇数的加法
*******************************************************
import urllib.request#爬虫
html=urllib.request.urlopen("http://www.t3sec.org.cn/match")#打开网页
html=html.read()
html=html.decode("utf-8")#转换编码
print(html)#打印下载的网页 
*******************************************************
import re
re.search(r'china','I love china')#正则表达式
re.search(r'chi.','I love china')#元字符.代表任意字符,可通过\.或[.]来寻找.
re.search(r'\d\d\d','I love 123 china')#寻找三个连续的数字
re.search(r'[aeiou]','I love china')#字符类,寻找指定字符类中的字符,[a-z]表示所有小写
re.search(r'[2-9]','I love 123 china')#在字符串中寻找数字2-9
re.search(r'ch{3}ina','chhhhina chhhina')#寻找c+三个h+ina,h{3,5}表示3到5个h
re.search(r'chin(a|b)','I love china')#寻找china或chinb
re.search(r'^chin','china is good')#开头必须是china,等于\A
re.search(r'hina$','china is good china')#结尾必须是china,等于\Z
re.search(r'(chin)\141','chinchina')#a的ASCII的十进制是97转换成八进制是141
p=re.compile(r'[a-z]')#编译正则表达式,编译成模式对象
p.findall('I love China')#找到所有小写打包成列表返回
re.findall(r'[^a-z]','I love China')#找到所有不是小写的打包成列表返回,[a-z^]表示匹配小写和^字符
re.search(r'<.+?>','<html><head></head></html>')#?表示非贪婪模式,尽可能少的匹配。+代表匹配一次或多次,等于{1,}
re.search(r'\bchina\b','china_(china.')#\b表示匹配单词边界,_会被当做字母
result=re.search(r'(\w+) (\w+) (\w+)',' 我 爱 China 123')#\w匹配所有语言的字符
result.group(2)#打印第二个字符
result.start()#输出匹配字符在原字符的开始位置
result.end()#输出匹配字符在原字符的结束位置
result.span()#输出匹配字符在原字符的位置范围
re.search(r'^(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|25[0-5]|2[0-4]\d)$','188.126.1.254')#匹配ip地址
*******************************************************
from urllib.request import Request,urlopen#异常处理
from urllib.error import URLError,HTTPError
req=Request('http://baidu.com')
try:
	response=urlopen(req)
except URLError as e:
	if hasattr(e,'reason'):
		print('reason: ',e.reason)
	elif hasattr(e,'code'):
		print('error code: ',e.code)
else:
    print(response.getcode())#没有问题
*******************************************************
i=1
while i<10:#python作业99乘法表
	j=1
	while j<=i:
		print("{}*{}={:<4}".format(j,i,i*j),end='\t')
		j+=1
	i+=1
	print("")
*******************************************************
for x in range(1,10):#输出等腰直角三角形
	for i in range(1,x):
		print("*",end=' ')
	print("*")
********************************************************
choose =int(input("1:偶数,2：奇数"))
if choose==1:
	rows=int(input("输入奇数"))
	for i in range(0,rows//2):
		for j in range(0,rows//2-i-1):
			print("",end="")