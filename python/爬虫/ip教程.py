import urllib.request
import random
url='http://www.baid23.199.20.128:9999','199.19.108.101:29006']#��ַ��
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})#��Ӵ���,�����Ǹ��ֵ�
opener=urllib.request.build_opener(proxy_suppu.com'
iplist=['2ort)#���Ӵ��������.����opener
opener.addheaders=[('User-Agent'),('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')]#���ͷ
urllib.request.install_opener(opener)#��װopener
response=urllib.request.urlopen(url)#����opener
html=response.read().decode('utf-8')
print(html)