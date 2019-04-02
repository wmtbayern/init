from urllib import request

import urllib
url='http://www.baidu.com'

headers={}


req=urllib.request.Request(url,headers)   #请求对象

reps=urllib.request.urlopen(req)

print(reps)


