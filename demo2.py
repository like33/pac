from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://re.jd.com/search?keyword=%E9%81%9B%E7%8B%97%E7%BB%B3'
driver = webdriver.Chrome()
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
title = soup.findAll('div', attrs={'class': 'commodity_tit'})
for i in title:
    print(i.text)