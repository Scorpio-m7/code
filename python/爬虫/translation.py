import urllib.parse
import json
import urllib.request
import time

while 1:
	content=input("输入需要翻译的,q!退出")
	if content=='q!':
		break

	url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	head={}
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
	data={}
	data['type']='AUTO'
	data['i']=['love']
	data['doctype']= ['json']
	data['version']=['2.1']
	data['keyfrom']=['fanyi.web']
	data['client']=['fanyideskweb']
	data['ue']=['UTF-8']
	data['typoResult']=['true']
	data=urllib.parse.urlencode(data).encode('utf-8')
	response=urllib.request.urlopen(url,data,head)#打开网页
	#response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
	html=response.read().decode('utf-8')
	print(html)
	#target=json.loads(html)
	#print("翻译结果：%s"(target['trans;ateResult'][0][0]['tgt']))
	time.sleep(5)