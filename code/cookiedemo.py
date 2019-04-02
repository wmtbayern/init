import urllib.request

from http import cookiejar

#第一步  创建cookie jar 对象  用来管理cookie


cookies=cookiejar.CookieJar()


# 创建cookie处理器
cookie_handler=urllib.request.HTTPCookieProcessor(cookies)

# opener打开器  ,主要是为了让opener 带上cookie

opener=urllib.request.build_opener(cookie_handler)
#其他步骤是一样的
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='http://www.baidu.com/'

req=urllib.request.Request(url,headers=headers)

response=opener.open(req)

# print(response.read().decode())

print(cookies)

#遍历所有的cookie
for cookie in cookies:
    print (cookie.name)
    print (cookie.value)