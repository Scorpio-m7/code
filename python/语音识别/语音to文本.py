import speech_recognition as sr
audio_file='1.wav'#语音文件
r=sr.Recognizer()
with sr.AudioFile(audio_file) as source:#读取语音文件
    audio=r.record(source)
try:
    print('你说了',r.recognize_sphinx(audio))#语音转换文本
    print('你说了', r.recognize_sphinx(audio,language='zh-CN'))#使用普通话输出
except Exception as e:
    print(e)