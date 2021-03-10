import urllib.request
import os
import random


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def get_page(url,h):
    html = url_open(url).decode('utf-8')
    a = html.find(f'comment-{h}')+8
    # a = html.find('commentlist') + 1797
    b = html.find('"', a)  # 从a之后找"
    print(html[a:b])
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 9:b + 3])
        else:
            b = a + 9
        a = html.find('img src', b)
    '''for each in img_addrs:
        print(each)'''
    print(img_addrs)
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        filename = filename.split('0')[-1]
        with open(filename, 'wb') as f:
            x = 'http:' + each
            img = url_open(x)
            f.write(img)


def download_mm(folder='ooxx', pages=100):
    if os.path.exists(folder) != True:
        os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    h=int(input("输入ooxx页面下的第一张图片的编号"))
    for i in range(pages):
        j=0
        while j<20:
            if ord(get_page(url,h-i-j)[0]) in range(47,58):
                page_num = int(get_page(url,h-i-j))
                break
            j+=1
            print(j)
        if j ==20:
            break

        page_url = f"http://jandan.net/t/{page_num}"
        img_addrs = find_imgs(page_url)
        if img_addrs != []:
            save_imgs(folder,img_addrs)


if __name__ == '__main__':
    download_mm()
