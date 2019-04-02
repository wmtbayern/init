import json
import urllib.request

# 注意请求头是字典的形式,,,可以有多个请求头
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}


for i in range(100):
    url = "https://movie.douban.com/j/" \
          "new_search_subjects?sort=T&range=0,10&tags=&start=%d" % (i) #查看原网页  d是请求的页数
    request=urllib.request.Request(url,headers=headers)
    #获取响应体  返回的是一个对象,要调用 read() 方法
    response=urllib.request.urlopen(request)
    #对响应体进行解码
    content=response.read().decode()  #要根据原网页的编码方式解码,python 默认是utf-8
    #返回的是json数据
    # print(content)
    data=json.loads(content)

    data_list=data.get('data')
    print(data_list)
    #获取到的一般都是列表 ,可以遍历,只获取自己想要的数据
    for item in data_list:
        #由键拿到对应的值
        title=item['title']

        casts=item['casts']

        print(('电影名字:{},主演:{}').format(title,casts))
