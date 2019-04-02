import urllib.request


# urllib.request.urlopen() 不能携带cookie 使用代理



#创建处理器对象  在处理器里面加上参数debuglevel=1  会开启debug log 日志, 会在终端打印输出 header 头
http=urllib.request.HTTPHandler(debuglevel=1)   #支持http
https=urllib.request.HTTPSHandler()  #支持https

#创建打开器对象
opener=urllib.request.build_opener(http)
#打开url
url="http://www.baidu.com/"
response=opener.open(url)
print(response.read().decode())
 #创建全局打开器
urllib.request.install_opener(opener=opener)

# pv page view 网页流量
# uv user visitor  以cookie 为区分  cookie 本身是一个文件  是header 头的属性 最大4K

