


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"
import json
import os
import urllib.request

def getData(url):
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    # for i in range(1, 3):
        # url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        # i * 20) + "&limit=20"
        #
    req = urllib.request.Request(url, headers=headers)
    # 获取响应体
    response = urllib.request.urlopen(req)

    html = response.read().decode()
    a=json.loads(html)
    # dir='dir'
    # os.chdir(dir)
    for item in a:

        urllib.request.urlretrieve(item['cover_url'],item['title']+'jpg')
if __name__ == "__main__":
    dir = 'dir'
    os.chdir(dir)
    for i in range(1, 3):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"

        getData(url)

#

