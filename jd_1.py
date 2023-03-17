from selenium import webdriver
import requests
from lxml import etree
from fake_useragent import UserAgent
import re
from selenium.webdriver.chrome.options import Options


def urls():
    ua = UserAgent()
    ans = []
    count = 0
    for j in range(10):
        url = 'https://movie.douban.com/top250?'
        header = {'user-agent': ua.random}
        params = {'start': count}
        res = requests.get(url, headers=header, params=params)
        html = etree.HTML(res.text)
        link = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
        ans = ans + link
        count = count + 25
    return ans


def get_page(url: str):
    op = Options()
    op.add_argument('--headless')
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    page = driver.page_source
    return page


def parse_page(page: str):
    html = etree.HTML(page)
    title = html.xpath('//*[@id="content"]/h1/span[1]/text()')
    direct = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
    screenwriter = html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
    starring = re.findall('rel="v:starring">(.*?)</a>', page)
    genre = re.findall('<span property="v:genre">(.*?)</span>', page)
    language = re.findall('<span class="pl">语言:<\/span>(.*?)<br\/>', page)
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    if len(language) != 0:
        language = regex.findall(language[0])
    release_date = re.findall('<span property="v:initialReleaseDate" content="(.*?)">', page)
    run_time = re.findall('<span property="v:runtime" content="(.*?)">', page)
    other_name = re.findall('<span class="pl">又名:<\/span>(.*?)<br\/>', page)
    score = re.findall('<strong class="ll rating_num" property="v:average">(.*?)<\/strong>', page)
    votes = re.findall('<span property="v:votes">(.*?)<\/span>', page)
    starts = re.findall('<span class="rating_per">(.*?)</span>', page)
    print(title)
    print(direct)
    print(screenwriter)
    print(starring)
    print(genre)
    print(language)
    print(release_date)
    print(run_time)
    print(other_name)
    print(score)
    print(votes)
    print(starts)
    with open('test.txt', 'a', encoding='utf-8') as fp:
        fp.write(str(title) + '\n' + str(direct) + '\n' + str(screenwriter) + '\n' + str(starring) + '\n' + str(
            genre) + '\n' + str(language) + '\n' + str(release_date) + '\n' + str(run_time) + '\n' + str(other_name))
        fp.write('\n' + str(score) + '\n' + str(votes) + '\n' + str(starts) + '\n')
        fp.write('*' * 66 + '\n')


if __name__ == '__main__':
    urls = urls()
    for i in urls:
        pages = get_page(i)
        parse_page(pages)
        print('*' * 50)