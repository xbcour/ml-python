import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}
data = {
    'kw': '字典'
}

response = requests.post(url=url, headers=headers, data=data)
for i in response.json()['data']:
    print(i['k'])
