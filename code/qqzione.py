import urllib.request

#cookie  放到请求头    模拟登陆状态
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='https://user.qzone.qq.com/2287228249'
http=urllib.request.HTTPHandler(debuglevel=1)



opener=urllib.request.build_opener(http)
req=urllib.request.Request(url,headers=headers)
response=opener.open(req)

print(response.read().decode())