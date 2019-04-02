import urllib.request



headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

proxy={'http':'http://121.233.207.142:9999'}

proxy_handler=urllib.request.ProxyHandler(proxies=proxy)


opener=urllib.request.build_opener(proxy_handler)
url='http://www.qfedu.com/'

req=urllib.request.Request(url,headers=headers)

response=opener.open(req)

html=response.read().decode()

print(html)