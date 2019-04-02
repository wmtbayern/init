import os
import urllib.request


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}




url="https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8&"#创建请求对象,
req=urllib.request.Request(url,headers=headers)
#获取响应体
response=urllib.request.urlopen(req)

html=response.read().decode()

dir = './'
os.chdir(dir)
file = urllib.request.urlopen(url).read()
open('alijob.html', 'wb').write(file)
print("获取数据成功")

