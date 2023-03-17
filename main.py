import re
import test
with open('【中科大】凌青老师的最优化理论视频教程,附带视频课件！！！.txt', 'r') as fp:
    info = fp.readlines()
fname = []
for i in info:
    fname.append(re.findall('.*\.mp4', i)[0].split('/')[-1])
urls = []
for i in info:
    urls.append(i.split('\n')[0])
for i in range(0, len(fname)):
    test.download(urls[i], fname[i])
