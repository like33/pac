import requests
from lxml import etree
import re
from header import header


url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
headers = header()
response = requests.get(url, headers=headers)
encode = re.findall('<meta http-equiv=\"Content-Type\" content=\"text/html; charset=(.*?)\" />', response.text)[0]
response.encoding = encode
html = etree.HTML(response.text)
title = re.findall('target=\"_blank\" title=\"(.*?)\">', response.text)
for i in title:
    print(i)