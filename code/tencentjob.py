import json
import urllib.request
import urllib.parse

import requests
from bs4 import BeautifulSoup

headers = {

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': '',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=2gr6022ot3vqqc3eb0qurkmbq5; pgv_pvi=7278042112; pgv_si=s82940928',
'Host': 'hr.tencent.com',
'Upgrade-Insecure-Requests': '1',
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

}

# url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"
url='https://hr.tencent.com/position.php?keywords=python&tid=0&lid=2218'



# for i in range(1,6):
#     params = {
#         "pageSize": 10,
#         "t": '0.8752307723219721',
#         "keyWord": "python",
#         "location": "深圳",
#         "pageIndex": i
#     }
#     data = urllib.parse.urlencode(params).encode()

req = urllib.request.Request(url,headers=headers)


response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, 'html.parser')

print(soup.find_all('table', class_='tablelist'))
jobList = soup.find_all('tr', class_=['even', 'odd'])
print(jobList)
for job in jobList:

    # 岗位名
    jobName = job.select("td:nth-of-type(1) > a")[0].text
    # url
    joburl = "https://hr.tencent.com/" + job.select("td:nth-of-type(1) > a")[0]['href']
    # 类型
    jobType = job.select("td:nth-of-type(2)")[0].text
    # 人数
    jobnum = job.select("td:nth-of-type(3)")[0].text
    # 地点
    jobAddr = job.select("td:nth-of-type(4)")[0].text

    print(jobName, joburl, jobType, jobnum, jobAddr)

# jobRes = soup.select("ul.squareli")
# print(soup)
# data_dict = json.loads(content)
#
# job_list = data_dict['returnValue']['datas']

# for job in  job_list:
#     degree = job.get('degree')
#     departmentName = job.get('departmentName')
#     requirement = job.get('requirement')
#     firstCategory = job.get('firstCategory')
#     workExperience = job.get('workExperience')
#
#     with open('ali.txt','a+',encoding='utf-8') as fp:
#         fp.write(degree+departmentName+requirement+firstCategory+workExperience+ "\n")
#         fp.flush() #write 必须回车才写 flush 能够不回车也往里写