#Filename=zhidog.py
import requests
r = requests.get("https://www.zhihu.com", headers = \
{ 'User-Agent':'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36' })
print r.status_code
