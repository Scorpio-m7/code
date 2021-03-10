import urllib.request
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_img(html):
    p=r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]|25[0-5])'
    iplist=re.findall(p,html)
    for each in iplist:
        print(each)
        
if __name__ == '__main__':
    url="https://chinaipaddress.wordpress.com/author/cnproxy/"
    get_img(url_open(url))
