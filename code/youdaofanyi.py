import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

english='what the fuck'
data={

'i': english,
'from': 'en',
'to': 'zh-CHS',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt':15541936784226,
'sign':'ec27ad219ba7e71e2bf604849a9741ec',
'ts': 1554193678422,
'bv': 'bc4909787425061aa1ebf29e3dd07b29',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME',
'typoResult': 'false',

}
response=requests.post(url,data=data,headers=headers)

dic=response.json()

tgt=dic['translateResult'][0][0]['tgt']

print(tgt)