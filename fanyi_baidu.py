import requests
from fake_useragent import UserAgent

url = "https://fanyi.baidu.com/sug"
data = {
    "kw": "dog"
}
ua = UserAgent()
header = {'user-agent': ua.random}
resp = requests.post(url, data=data, headers=header)
data_list = resp.json()['data']
for item in data_list:
    print(f"{item['k']}: {item['v']}")