import urllib.parse
import time
import urllib.request#爬虫

while 1:
    a = input("输入横像素")
    if a=='q':
        break
    b=input("输入竖像素")
    url=f'http://placekitten.com/{a}/{b}'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
    data = {}
    data['type'] = 'AUTO'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response=urllib.request.urlopen(url)#打开网页
    cat_img=response.read()
    print(response)
    with open(f'cat_{a}_{b}.jpg','wb') as f:
        f.write(cat_img)#把图片保存到cat_500_600.jpg

    #time.sleep(5)#模拟人访问，速度变慢
    #print(response.geturl())#获取地址
    #print(response.info())#打印http头部
    #print(response.getcode())#网页状态码
