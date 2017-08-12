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
           }#这个字典没有顺序。
    #ectdog.sort() #这里报错了。
    numberdog= 0
    for a,b  in ectdog.items():
        #a=int(input('the code of %s:' %a ))   #这里好像没有什么用
        ectdog[a]=int(input('the code of %s:' %a ))
    for a,b  in ectdog.items():
        numberdog=numberdog+b
    for a,b  in ectdog.items():
        print (b)
    print ('共有')
    print(7-numberdog)
    print ('个倒立文字。')
    kdog=0
    ll=''
    if ectdog['zf1']==0 :
        ll='[12.95,15]'
        kdog=1
    else:
        pass
    if ectdog['zf2']==0 :
        if kdog==0:
            ll=ll+'[36.1,16.1]'
            kdog=1
        else:
            ll=ll+',[36.1,16.1]'
    else:
        pass
    if ectdog['zf3']==0 :
        if kdog==0:
            ll=ll+'[57.16,24.44]'
            kdog=1
        else:
            ll=ll+',[57.16,24.44]'
    else:
        pass
    if ectdog['zf4']==0 :
        if kdog==0:
            ll=ll+'[84.52,19.17]'
            kdog=1
        else:
            ll=ll+',[84.52,19.17]'
    else:
        pass
    if ectdog['zf5']==0 :
        if kdog==0:
            ll=ll+'[108.72,28.64]'
            kdog=1
        else:
            ll=ll+',[108.72,28.64]'
    else:
        pass
    if ectdog['zf6']==0 :
        if kdog==0:
            ll=ll+'[132.95,24.44]'
            kdog=1
        else:
            ll=ll+',[132.95,24.44]'
    else:
        pass
    if ectdog['zf7']==0 :
        if kdog==0:
            ll=ll+'[151.89,23.38]'
            kdog=1
        else:
            ll=ll+',[151.89,23.38]'
    else:
        pass



#random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
     data = {
        'phone_num': phone_num,
        'password': password,
        '_xsrf': xsrf,
        "captcha": captcha,
        'captcha_type':cn}




    #



    session.cookies.save()
else:
    session.cookies.save()
    pass
