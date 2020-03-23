from urllib.request import urlopen

url = 'http://www.python3.vip/doc/tutorial/python/0004/'
response = urlopen(url)
info = response.read()
print(info.decode('utf-8', 'ignore'))
