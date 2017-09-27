#Filename=zhidog.py
import requests,time, os ,random
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
headerscat={
"Host": "www.zhihu.com",
"Referer": "https://www.zhihu.com/collections/mine",
'User-Agent': 'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'


}
r = session.get("https://www.zhihu.com/inbox", headers = headerscat )
print (r.status_code)
for name,value in r.headers.items():
    print ("%s:%s" % (name, value))

eepdog=r.content#这里的数据类型是bytes，需要用decode转化成字符串str
#print (eepdog.decode())
session.cookies.save()
#下面提取验证码图片
dog=input('是否登录：')
if dog=='y':
    soup = BeautifulSoup(r.content, "html.parser")
    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    print (xsrf)
    phone_num=input('手机号：')
    password=input('password:')
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
    print('字符串的第一次拼接：')
    print(ll)
    print('第二次字符串拼接')
    captcha='{"img_size":[200,44],"input_points":['+ll+']}'
    print(captcha)


#random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
    data = {
        'phone_num': phone_num,
        'password': password,
        '_xsrf': xsrf,
        "captcha": captcha,
        'captcha_type':'cn'}
    postdog='https://www.zhihu.com/login/phone_num'
    response = session.post(postdog, data=data, headers=headers)
    login_code = response.json()
    print(login_code['msg'])
    for i in session.cookies:
        print(i)
    session.cookies.save()


    #



    session.cookies.save()
else:
    session.cookies.save()
    pass

for pigdog in range(1,14):
    pigurl=str(pigdog)
    dogurl="https://www.zhihu.com/collection/172453801?page="+pigurl
    rapdog= session.get(dogurl, headers = headers )
    #print(rapdog.content.decode())
    soup2 = BeautifulSoup(rapdog.content, "html.parser")
    xsrf2 = soup2.find('input', attrs={"name": "_xsrf"}).get("value")
    print(xsrf2)
    session.cookies.save()
    #upsdog=soup.find_all('div',content='data-aid')#.get("content")
    #print(upsdog)
    upsdog=soup2.find_all('div', attrs={"class":"zm-item-answer "})#提取开始，类似数组的东西。
    dognumber=0
    for idog in upsdog :
        id666=idog.get('data-aid')
        print(id666)
        dognumber=dognumber+1
    ups2dog=soup2.find_all('div', attrs={"class":"zm-item-answer "})
    for ipig in ups2dog :
        id777=ipig.get('data-atoken')
        print (id777)
    print(upsdog[0].get('data-aid'))
    headersdog = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/collection/172453801",
        'User-Agent': 'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36',
         'X-Xsrftoken':'36992469-649e-404b-8433-afc3cebcfa1e',
         '_xsrf': xsrf2
    }
    for i in range(0, dognumber):
        session = requests.session()
        session.cookies = cookiejar.LWPCookieJar(filename='/home/yu/aadog/cookies.txt')
        try:
            session.cookies.load(ignore_discard=True)
        except :
            print ("load cookies failed")

        dogdata={
        'type':'answer',
        'id':str(upsdog[i].get('data-aid')),
        'urlToken':str(ups2dog[i].get('data-atoken')),
        'reason':'politics',
        'source':'web',
        '_xsrf': xsrf2
        }
        print (str(upsdog[i].get('data-aid')))
        print(ups2dog[i].get('data-atoken'))
        responsedog2 = session.post("https://www.zhihu.com/report", data=dogdata, headers=headersdog)
        #report_code = responsedog2.json()
        print(i)
        print(responsedog2.content.decode())
        #print(report_code['msg'])
        time.sleep(20+random.uniform(-18,20))
        session.cookies.save()
    time.sleep(30+random.uniform(-10, 10))

    print ('end')
