import requests
from pyquery import PyQuery as pq
import os
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

#下载图片的模块
def Download_the_module(file,tehurl):
    count = 1
    # 进入网站下载图片
    The_second_request = requests.get(tehurl, headers=headers).text
    # 下载
    The_doc = pq(The_second_request)
    # 初始化 传入字符串
    Download_the_pictures = The_doc('.big_img')
    # 通过选择器来获取目标内容
    Take_out_the=pq(Download_the_pictures.html())
    # 获取 img 标签  find --> 查找嵌套元素
    Extract_the=Take_out_the.find('img').items()
    # 得到那个图片
    for i in Extract_the:
        save=i.attr('src')
        #print(save)
        The_sponse=requests.get(save,headers=headers)
        The_name='图片/'+file
        Save_the_address = str(The_name)
        # 检测是否有image目录没有则创建
        if not os.path.exists(Save_the_address):

            # 指定路径
            os.makedirs('图片/' + file )
        else:


            with open(Save_the_address+'/%s.jpg'%count,'wb')as f:
                f.write(The_sponse.content)
                print('已经下载了%s张'%count)
            count += 1
#爬取地址
def Climb_to_address(page,b):

    URL='https://www.169tp.com/gaogensiwa/list_3_%s.html'%page
    sponse=requests.get(URL,headers=headers)
    # 解码
    sponse.encoding='gbk'
    # 响应内容为 text
    encodin=sponse.text
    # 可以通过传入 字符串、lxml、文件 或者 url 来使用PyQuery
    doc=pq(encodin)
    extract=doc('.pic').items()
    for i in extract:
        #文件名
        The_file_name=i.text()
        #提取到的网站
        The_url=i.attr('href')

        Download_the_module(The_file_name,The_url)

#一共有616页
a=int(input('请输入开始爬取的页数:'))
b=int(input('请输入结束爬取的页数:'))
Climb_to_address(a,b)