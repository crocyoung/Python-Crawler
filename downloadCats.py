import urllib.request

#req = urllib.request.Request("http://www.baidu.com/img/bd_logo1.png")
response = urllib.request.urlopen("http://www.baidu.com/img/bd_logo1.png")

baidu_img = response.read()

with open('BaiDu.png', 'wb') as f:
    f.write(baidu_img)
