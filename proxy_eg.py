import urllib.request
import random
import json

while True:
    url = "http://www.whatismyip.com.tw"
    # random pick an proxy
    ipList = ['218.106.96.201:81' , '218.106.96.203:81' , '218.106.96.204:80']
    ip_port = random.choice(ipList)
    proxy_support = urllib.request.ProxyHandler({'http' : ip_port})
    # use some configure-setted opener to open an url. wen can set the headers and visitor ip address
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')]

    # install this new setted opener () , default use this new setted opener to open url  
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    #target = json.loads(html)
    print(html)
