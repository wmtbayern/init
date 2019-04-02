# requests库继承了urllib2 的所有特性，支持http 连接保持，连接池  支持文件上传
# ，支持国际化   功能比url库更加强大  社区活跃

import requests

#get 请求
url='http://baidu.com/'
res=requests.get(url)
# print(res)
# <Response [200]>

print(res.status_code)   #200

# print(res.url)        #url
# print(res.cookies)   #<RequestsCookieJar[]>
# print(type(res.text))   #str
# print(res.content)#二进制的数据
# print(res.content.decode())
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
params={
    'wd':'岛国教育片'

}
response=requests.get('http://www.baidu.com/s',params,headers=headers)

print(response.content.decode())
