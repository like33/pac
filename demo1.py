from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = 'https://wallhaven.cc/toplist?page=2'
driver = webdriver.Chrome()
driver.get(url)
temp_height = 0
while True:
    driver.execute_script("window.scrollBy(0,1500)")
    time.sleep(3)
    check_height = driver.execute_script(
        "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    if check_height == temp_height:
        break
    temp_height = check_height
text = driver.page_source
soup = BeautifulSoup(text, 'lxml')
links = soup.findAll('a', attrs={'class': 'preview'})
urls = []
for i in links:
    urls.append(i.get('href'))
with open('links.txt', 'w') as fp:
    for i in urls:
        print(i)
        fp.write(i+'\n')
