import urllib.request
import urllib.parse
import json




#while(1):
#header = { }
#header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"

while True:                                                            
    #content = input("请输入要翻译的内容:  ")
    content = "hello"
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://dict.youdao.com/"
    data = { }
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    # parse the all info into data object
    data = urllib.parse.urlencode(data).encode('utf-8')

    #req = urllib.request.Request(url, data, header)
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')


    response = urllib.request.urlopen(url,  data)
    html = response.read().decode('utf-8')
                                                               
    target = json.loads(html)
    print("翻译结果： %s"  %(target['translateResult'][0][0]['tgt']))




#{'errorCode': 0, 'translateResult': [[{'tgt': '爱你宝贝', 'src': 'l ove you baby'}]], 'type': 'EN2ZH_CN', 'elapsedTi
#>>> target['translateResult']
#[[{'tgt': '爱你宝贝', 'src': 'l ove you baby'}]]
#>>> target['translateResult'][0]
#[{'tgt': '爱你宝贝', 'src': 'l ove you baby'}]
#>>> target['translateResult'][0][0]['tgt']
#'爱你宝贝'
