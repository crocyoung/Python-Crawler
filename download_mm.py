import urllib.request
import random
import os

# open url retrun html
def url_open(url):
    '''
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read( )
    print(url)
    return html

    '''
    ipList = ['218.106.96.201:81' , '218.106.96.203:81' , '218.106.96.204:80']
    ip_port = random.choice(ipList)
    proxy_support = urllib.request.ProxyHandler({'http' : ip_port})
    # use some configure-setted opener to open an url. wen can set the headers and visitor ip address
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')]

    # install this new setted opener () , default use this new setted opener to open url  
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()

    return html


    
# get newest page number from ooxx html
def get_page(url):
      html = url_open(url).decode('utf-8')

      pre = html.find('current-comment-page') + 23    # >[
      aft = html.find(']', pre)                                          # from a to ']'

      return html[pre : aft]                                            # return the number in html within the range



def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    pre = html.find('img src=')

    while pre != -1:
        aft = html.find('.jpg' , pre , pre + 255)  # in case no jpg postfix
        if aft != -1:
            img_addrs.append(html[pre+9 : aft+4])
        else:
            aft = pre + 9

        pre = html.find('img src=' ,  aft)

    for each in img_addrs:
        print(each)

    return img_addrs 
         


            
def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)





def download_mm(folder='mm_picture' , pages=10):
    # create folder,  change directory
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jandan.net/ooxx/'
    #url = 'http://www.baidu.com'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-'+ str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)



        
if __name__ == '__main__' :
    download_mm( )
        
        
