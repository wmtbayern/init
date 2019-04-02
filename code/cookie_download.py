import urllib.request

from http import cookiejar


file='baidu.txt'
cookie=cookiejar.LWPCookieJar(filename=file)

handler=urllib.request.HTTPCookieProcessor(cookie)

opener=urllib.request.build_opener(handler)

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url='http://www.baidu.com/'

req=urllib.request.Request(url,headers=headers)
response=opener.open(req)

print(response)

cookie.save()