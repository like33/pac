import requests
from fake_useragent import UserAgent
import re

url = 'https://checkip.synology.com/'
ua = UserAgent()
header = {'user-agent': ua.random}
res = requests.get(url, headers=header, timeout=3)
print(re.findall('<body>Current IP Address: (.*?)</body>', res.text)[0])
