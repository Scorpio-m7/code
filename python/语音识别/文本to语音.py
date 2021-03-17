import pyttsx3 as pyttsx#使用pyttsx实现
engine=pyttsx.init()#初始化
engine.say('大家好')#文字转化语音
engine.runAndWait()#运行
#***********************************
from win32com.client import  Dispatch#导入Dispatch对象
sperker=Dispatch('SAPI.SpVoice')#生成对象
sperker.Speak('我是zt')
del sperker#释放对象