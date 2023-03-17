import requests
import time
user_name = 'HY19891733263'
passwd = '289051'
print('1.中国移动')
print('2.校园网')
selection = eval(input())
if selection == 1:
    user_name = user_name + '@cmcc'
elif selection == 2:
    user_name = user_name + '@xyw'
base_url = 'http://10.0.6.2/drcom/login?'
cur_time = int(time.time())
params = {'callback': 'dr1676876461989',
          'DDDDD': user_name,
          'upass': passwd,
          '0MKKey': '123456',
          'R1:': '0',
          'R3': '0',
          'R6': '0',
          'para': '00',
          'v6ip_': '1676876456181'
          }
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
resp = requests.get(base_url, headers=header, params=params)
print(resp.text)
