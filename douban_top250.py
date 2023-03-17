import time
import requests
from lxml import etree
from fake_useragent import UserAgent
import re


ua = UserAgent()


def info(url):
    header = {'user-agent': ua.random}
    res = requests.get(url, headers=header)
    time.sleep(1)
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    title = html.xpath('//*[@id="content"]/h1/span[1]/text()')
    direct = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
    screenwriter = html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
    starring = re.findall('rel="v:starring">(.*?)</a>', res.text)
    genre = re.findall('<span property="v:genre">(.*?)</span>', res.text)
    language = re.findall('<span class="pl">语言:<\/span>(.*?)<br\/>', res.text)
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    if len(language) != 0:
        language = regex.findall(language[0])
    release_date = re.findall('<span property="v:initialReleaseDate" content="(.*?)">', res.text)
    run_time = re.findall('<span property="v:runtime" content="(.*?)">', res.text)
    other_name = re.findall('<span class="pl">又名:<\/span>(.*?)<br\/>', res.text)
    score = re.findall('<strong class="ll rating_num" property="v:average">(.*?)<\/strong>', res.text)
    votes = re.findall('<span property="v:votes">(.*?)<\/span>', res.text)
    starts = re.findall('<span class="rating_per">(.*?)</span>', res.text)
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


def urls():
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


if __name__ == '__main__':
    us = urls()
    for i in us:
        info(i)
        print('*' * 50)
