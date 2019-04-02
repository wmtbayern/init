import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


proxy={'http':'http://121.233.207.142:9999'}


url='http://www.qfedu.com/'

response=requests.get(url,headers=headers,proxies=proxy)
print(response.text)