import requests
num = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wi'
                         'n64; x64) AppleWebKit/537.36 (KHT'
                         'ML, like Gecko) Chrome/80.0.3987.1'
                         '22 Safari/537.36', 'Cookie': 'user[openid'
                         ']=1; user[logintype]=w; JumpM1=1; Hm_lvt_63a93376491d073b73b901'
                         '3396ad02a8=1585152512; us'
                         'er[nickname]=Communist; user[uid]=3061'
                         '440; user[pkey]=8ef429c149feb2395b5f1'
                         '5a93e9e6108; user[pass]=2c38648d0a1623bfba513b1a2f916e4c; u'
                         'ser[timeout]=1585789597; user[timecheck]=1585185397; Hm'
                         '_lvt_727bf79ab8e96a37e6486fccd3f61c22=1585152525,1585182115'
                         ',1585184773,1585184791; user[timewcheck]=1585186250; PHPSESS'
                         'ID=btr2lmhln6uink9gm50bt1ofa2', 'Accept': 'text/html,applicat'
                         'ion/xhtml+xml,applic'
                         'ation/xml;q=0.9,ima'
                         'ge/webp,image/apng,'
                         '*/*;q=0.8,applicati'
                         'on/signed-exchange;'
                         'v=b3;q=0.9'}
# 777 786
for i in range(704, 712):
    url = 'https://paper.i21st.cn/download/21se3_' + str(i) + '.pdf'
    book = requests.get(url, headers=headers)
    print('正在爬取第' + str(num) + '份报纸')
    f = open('E:/PYstudy/21c1/' + str(num) + '.pdf', 'ab')
    f.write(book.content)
    f.close()
    num += 1
