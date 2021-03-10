import urllib.request
import re
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html
def get_img(html):
    p = r'(.*?)/p>'
    imglist=re.findall(p,html)
    for each in imglist:
        print(each)
        with open(f'1.TXT', 'a+') as f:
            f.write(each+"\n")
if __name__ == '__main__':
    url="https://wenku.baidu.com/view/dfa5d055a0c7aa00b52acfc789eb172dec639924.html"
    get_img(url_open(url))