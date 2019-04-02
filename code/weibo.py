import os
import urllib.request

import http.cookiejar

import urllib.parse


#创建cookiejar 对象

cookie=http.cookiejar.CookieJar()

#处理器对象
#这样才可以携带cookie
handler=urllib.request.HTTPCookieProcessor(cookie)

#根据处理器，创建打开器对象

opener=urllib.request.build_opener(handler)

#用代码模拟登陆

url = "https://weibo.cn/6388179289/info"
data={

    "username":"17701256561",
    "password":"lizhibin666",
    "savestate":1,
    "r":"https://weibo.cn/",
    "ec":0,
    "entry":"mweibo",
    "mainpageflag":1,
    "client_id":"",
    "code":"",
    "qq":"",
    "hff":"",
    "hfp":"",
    "wentry":"",
    "loginfrom":"",
    "pagerefer":"",

}

#请求头  登陆状态的请求头不一样
# headers = {
#     "Origin": "https://passport.weibo.cn",
#     "Accept": "*/*",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Connection": "keep-alive",
#     "Host": "passport.weibo.cn",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Referer":"https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# }

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

req=urllib.request.Request(url,headers=headers)
response=opener.open(req)
# file=response.read()

# dir='./'
# os.chdir(dir)
# open('weibo.html','wb').write(file)
print(response.read().decode('gb2312'))
# print(response.read().decode('gb2312'))
print(cookie)

