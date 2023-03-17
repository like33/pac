from wallheaven import *

if __name__ == '__main__':
    page = parse_page('https://wallhaven.cc/random?seed=Pwkadc&page=2')
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': '_pk_id.1.01b8=18e2ddcf3e6002d6.1677507755.; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkQwSmc3bkFxUGZCYTkwait3Qmh3T1E9PSIsInZhbHVlIjoiN3kwRFJiQWFvXC9uN0RjV0VnM3JoNXpRT0FzdldneE9nellXQjdiWllkNFU4MjhXeElsK2g1QzQ1SEE1b3dLS1YiLCJtYWMiOiI4NTk1Yzk1NTk5MzVkZjUzNjYwYzViMGNiZmZlZDE0NDc1MzhkNjVhMzA5N2YwZjkxNGM0NTg0YmI2ODg2ZTBhIn0=; wallhaven_session=eyJpdiI6IlVDNzZKelF4dXRqVkQ1a1ZrbDVpalE9PSIsInZhbHVlIjoibGZFOGwwdFBXdWJRMXZ3dVhNNEdzaHQxUDRaTitIOWdpaVE3K20wOHVpbnJ6M3FiV0xjYWZ3MnVxbnM2ZXo0RCIsIm1hYyI6IjkwNzczNjA3Zjc5Yzc1NTVjOGZmMmZlZWNjNzMxMjAzMzljYzlkN2FjNjk5NzcxMzYzZGE3ODM2ZGJmMzQ3MjgifQ==',
        'referer': 'https://wallhaven.cc/'
    }
    count = 1
    print(page)
    for i in range(1, page+1):
        print(f'正在解析第{i}页')
        all_url = p(i)
        print(f'共解析到{len(all_url)}张图片')
        for j in all_url:
            print(f'开始解析:{j}')
            img_url = parse(j)
            print(f'解析结果为:{img_url}, 开始下载第{count}张')
            if img_url == '':
                continue
            else:
                downloads(img_url, headers=header)
                print()
                count = count+1