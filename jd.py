import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

with open('jd.txt', 'w', encoding='utf-8') as fp:
    fp.write('标题,价格,店铺,链接,点击\n')
    for index in range(1, 199, 2):
        print(f'第{index}页')
        url = 'https://list.jd.com/list.html?'
        ua = UserAgent()
        ins = 1
        headers = {'user-agent': ua.random}
        params = {'cat': '670,671,673', 'page': index, 's': ins, 'click': 0}
        res = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(res.text, 'lxml')
        info = soup.find_all('div', attrs={'id': 'J_goodsList'})
        goods_info = []
        count = 0
        for i in info:
            infos = i.findNext('ul', attrs={'class': 'gl-warp clearfix'})
            for j in infos:
                if not j.findNext('div', attrs={'class': 'p-name p-name-type-3'}) is None:
                    title = j.findNext('div', attrs={'class': 'p-name p-name-type-3'}).findNext('a').findNext('em').text
                    price = j.findNext('div', attrs={'class': 'p-price'}).findNext('strong').findNext('i').text
                    commit = j.findNext('div', attrs={'class': 'p-commit'}).findNext('strong').findNext('a').get(
                        'onclick')
                    urls = j.findNext('div', attrs={'class': 'p-name p-name-type-3'}).findNext('a').get('href')
                    if not urls.startswith('https:'):
                        urls = 'https:' + urls
                    shop = j.findNext('div', attrs={'class': 'p-shop'}).findNext('span').findNext('a').text
                    information = title + '\t' + '价格:' + price + '\t' + '点击量:' + commit + '\t' + '链接:' + urls + '\t' + shop
                    if information == '':
                        continue
                    else:
                        print(information)
                        fp.write(f'{title},{price},{shop},{urls},{commit}\n')
                        time.sleep(0.1)
        time.sleep(3)
