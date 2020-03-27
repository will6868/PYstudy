import requests
from pyquery import PyQuery as pq
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                         'WebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


def index(page):
    url = 'https://www.quanjing.com/creative/topic/' + str(page)
    response = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
    doc = pq(response)
    data = doc('.gallery div img').items()
    num = 1
    for i in data:
        data2 = i.attr('src')
        img = requests.get(data2)
        f = open('E:/PYstudy/cc/' + str(num) + '.jpg', 'ab')
        f.write(img.content)
        f.close()
        print('正在爬取第' + str(num) + '张图片')
        num += 1


input_page = input('Which page do you want?')
index(input_page)
