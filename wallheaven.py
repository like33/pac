import requests
from lxml import etree
import re
import time, multiprocessing
import os
from bs4 import BeautifulSoup
from multiprocessing import Process
from contextlib import closing

requests.packages.urllib3.disable_warnings()
session = requests.session()


def crawl_page():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    url = 'https://wallhaven.cc/random?seed=Pwkadc&page=2'
    url = re.findall('(.*)page', url)[0]
    params = {'page': 2}
    res = session.get(url, headers=header, params=params)
    html = etree.HTML(res.text)
    img_url = []
    page = html.xpath('//*[@id="thumbs"]/section[1]/header/h2/text()[2]')
    page = eval(re.findall('\\d+', page[0])[0])
    for i in range(1, page + 1):
        params = {'page': i}
        res = session.get(url, headers=header, params=params, verify=False)
        html = etree.HTML(res.text)
        img_url.extend(html.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/a/@href'))
        tmp = html.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/a/@href')
        print(f'正在爬取{i}/{page}, {len(tmp)}')
        for j in html.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/a/@href'):
            print(j)
        time.sleep(2)
    return img_url


def download(url: str):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    name = url.split('/')[-1]
    os.path.exists('./img') or os.mkdir('./img')
    res = session.get(url, headers=header, verify=False)
    with open('./img/' + name, 'wb') as fp:
        fp.write(res.content)


def parse(url: str):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    res = session.get(url, headers=header, verify=False)
    soup = BeautifulSoup(res.text, 'lxml')
    link = soup.findAll('img', attrs={'id': 'wallpaper'})
    tmp = ''
    for i in link:
        tmp = i.get('src')
    return tmp


def parse_page(url: str):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    url = re.findall('(.*)page', url)[0]
    params = {'page': 2}
    res = session.get(url, headers=header, params=params, verify=False)
    html = etree.HTML(res.text)
    page = html.xpath('//*[@id="thumbs"]/section[1]/header/h2/text()[2]')
    page = eval(re.findall('\\d+', page[0])[0])
    return page


def p(page: int):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    url = 'https://wallhaven.cc/random?seed=Pwkadc&page=2'
    url = re.findall('(.*)page', url)[0]
    params = {'page': page}
    res = session.get(url, headers=header, params=params)
    html = etree.HTML(res.text)
    return html.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/a/@href')


def downloads(download_url, headers):
    os.path.exists('./img') or os.mkdir('./img')
    name = download_url.split('/')[-1]
    with closing(requests.get(download_url, verify=False, stream=True, headers=headers)) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        with multiprocessing.Manager() as mng:
            mdict = mng.dict()
            mdict['data_bytes'] = 0
            mdict['exit'] = False
            process = Process(target=cron, args=(name, content_size, mdict))
            process.start()
            with open('./img/' + name, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    mdict['data_bytes'] += len(data)
            mdict['exit'] = True
            process.join(3)
            process.terminate()


def cron(file_name, content_size, mdict):
    interval = 0.5
    content_size_formated = format_bytes_num(content_size)
    data_bytes_prev = mdict['data_bytes']
    time_prev = time_now = time.time()
    while True:
        data_bytes = mdict['data_bytes']
        try:
            speed_num = (data_bytes - data_bytes_prev) / (time_now - time_prev)
        except ZeroDivisionError:
            speed_num = 0
        data_bytes_prev = data_bytes
        time_prev = time_now

        speed = format_bytes_num(speed_num)
        data_bytes_formated = format_bytes_num(data_bytes)
        persent = data_bytes / content_size * 100  # 当前下载百分比
        done_block = '█' * int(persent // 2)  # 共显示50块，故以2除百作五十，计为所下载的显示块数
        print(
            f"\r {file_name} ----> [{done_block:50}] {persent:.2f}%   {speed}/s   {data_bytes_formated}/{content_size_formated}",
            end=" ")

        # 收到信号时退出
        if mdict['exit']: break

        # 消磨剩余时间
        time_now = time.time()
        sleep_time = time_prev + interval - time_now
        if sleep_time > 0:
            time.sleep(sleep_time)
            time_now = time.time()  # 避免误差


def format_bytes_num(bytes_num):  # 格式化为合适的数值大小与单位
    i = 0
    while bytes_num > 1024 and i < 9 - 1:
        bytes_num /= 1024
        i += 1
    unit = ('B', 'kiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')[i]
    return "%.2f" % bytes_num + unit