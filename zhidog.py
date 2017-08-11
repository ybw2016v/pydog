#Filename=zhidog.py
import requests,time, os
#import cookies
from http import cookiejar
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='/home/yu/aadog/cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except :
    print ("load cookies failed")
#######################
r = requests.get("https://www.zhihu.com/#signin", headers = \
{ 'User-Agent':'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36' })
print (r.status_code)
for name,value in r.headers.items():
    print ("%s:%s" % (name, value))
eepdog=r.content#这里的数据类型是bytes，需要用decode转化成字符串str
#print (eepdog.decode())




session.cookies.save()
