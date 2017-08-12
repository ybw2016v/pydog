#Filename=zhidog.py
import requests,time, os
#import cookies
from bs4 import BeautifulSoup
from http import cookiejar
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': 'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'
}
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='/home/yu/aadog/cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except :
    print ("load cookies failed")
#######################
r = session.get("https://www.zhihu.com/#signin", headers = headers )
print (r.status_code)
for name,value in r.headers.items():
    print ("%s:%s" % (name, value))
soup = BeautifulSoup(r.content, "html.parser")
xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
print (xsrf)
eepdog=r.content#这里的数据类型是bytes，需要用decode转化成字符串str
#print (eepdog.decode())
#下面提取验证码图片
dog=input('是否登录：')
if dog=='y':
    print('正在登录……')
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (time.time() * 10000)
    redog = session.get(captcha_url, headers=headers)
    #with open('captcha.gif', 'wb') as f: 已废弃
    #print (redog.content) #一坨屎乱码
    with open('captcha.gif', 'wb') as f:
        f.write(redog.content)
    ectdog={ 'zf1' : 1,
             'zf2' : 1,
             'zf3' : 1,
             'zf4' : 1,
             'zf5' : 1,
             'zf6' : 1,
             'zf7' : 1
           }
    ectdog.sort()
    for a,b  in ectdog.items():
        b=input('the code of%s:' %a )





    #



    session.cookies.save()
else:
    pass
