from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://music.163.com/#/discover/toplist'
driver = webdriver.Chrome()
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
info = soup.findAll('')
