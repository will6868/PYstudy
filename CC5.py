import requests
from pyquery import PyQuery as pq
url = 'https://paper.i21st.cn/pdf_21se1_785_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wi'
                         'n64; x64) AppleWebKit/537.36 (KHT'
                         'ML, like Gecko) Chrome/80.0.3987.1'
                         '22 Safari/537.36'}
response = requests.get(url, headers=headers).content.decode('utf-8', 'ignore')
doc = pq(response)
data = doc('.paperbody div a')
data2 = data.attr('href')
print(data2)
