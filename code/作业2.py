import re
import time

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示：
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)
import urllib.request


# def getData(url):
headers = {
    "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "https://www.qiushibaike.com/text/page/1/"
req = urllib.request.Request(url, headers=headers)

response=urllib.request.urlopen(req)
html=response.read().decode()
regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)

nameCom = re.compile('<h2>(.*?)</h2>', re.S)

contentCom = re.compile('<span>(.*?)</span>', re.S)

content_list=re.findall(contentCom,html)
name_list=re.findall(nameCom,html)

all=[name_list+content_list]
print(all)

# for i in content_list:
#     print(i)
#
#
# for item in name_list:
#     print(item)

#
# if __name__ == "__main__":
#
#     # 所有数据
#     allData = []
#     # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]
#
#     # 遍历每一页的数据
#     for i in range(1, 4):
#         url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
#         list1 = getData(url)
#         allData.extend(list1)
#
#         time.sleep(0.5)
#
#
#     # 遍历allData 把数据显示
#     for dict1 in allData:
#         print("%s 说： %s" % (dict1["name1"], dict1["content"]))



