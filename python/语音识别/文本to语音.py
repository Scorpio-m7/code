import pyttsx3 as pyttsx#使用pyttsx实现
engine=pyttsx.init()#初始化
engine.say('大家好')#文字转化语音
engine.runAndWait()#运行
#***********************************
from win32com.client import  Dispatch#导入Dispatch对象
sperker=Dispatch('SAPI.SpVoice')#生成对象
str=open("1.txt", encoding="utf-8").read()#打开文本
sperker.Speak(str)#朗读
sperker.Speak('我是赵桐')
del sperker#释放对象
#***********************************
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
engine=CreateObject("SAPI.SpVoice")
stream=CreateObject('SAPI.SpFileStream')#输出流
stream.open('1.wav',SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream=stream#接通管道
f=open('1.txt','r',encoding='utf-8')#读取文本内容
engine.speak(f.read())#输出到1.wav
f.close()#关闭文件
stream.close()#输出流关闭
