import requests
from fake_useragent import UserAgent
import re

url = 'https://www.qidian.com/xianxia/'
ua = UserAgent()
header = {'user-agent': ua.random}
res = requests.get(url, headers=header)
title = re.findall('<a href=\".*\" data-eid=\"qd_F24\" data-bid=\".*\" target=\"_blank\" title=\".*\">(.*?)</a>', res.text)
print(title)
