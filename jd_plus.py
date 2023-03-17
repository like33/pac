from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


url = 'https://list.jd.com/list.html?cat=670%2C677%2C688&page=3&s=57&click=0'
op = Options()
op.add_argument('--headless')
driver = webdriver.Chrome(options=op)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
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
