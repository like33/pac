from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://list.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmate50&enc=utf-8&spm=2.1.8%27'
driver = webdriver.Chrome()
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
title = soup.findAll('i', attrs={'class': 'promo-words'})
titles = []
for i in title:
    titles.append(i.text)
shop = soup.findAll('a', attrs={'class': 'curr-shop hd-shopname'})
shops = []
for i in shop:
    shops.append(i.text)
infos = zip(shops, titles)
with open('jd_gooods.txt', 'w') as fp:
    for i in infos:
        print(i)
        fp.write(str(i)+'\n')