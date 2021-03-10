import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_img(html):
    p=r'<img src="([^"]+\.jpg)"'
    imglist=re.findall(p,html)
    for each in imglist:
        filename=each.split("/")[-1]
        urlname='http:'+each
        print(each)
        urllib.request.urlretrieve(urlname,filename,None)

if __name__ == '__main__':
    folder='ooxx'
    if os.path.exists(folder) != True:
        os.mkdir(folder)
    os.chdir(folder)
    url="http://jandan.net/ooxx"
    get_img(url_open(url))
