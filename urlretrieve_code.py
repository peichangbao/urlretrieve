import urllib.request
from lxml import etree
import requests
def Schedule(blocknum,blocksize,totalsize):
    '''blocknum:已经下载的数据块
    blocksize:数据块的大小
    totalsize:远程文件的大小'''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度: %d' % per)

user_agent = 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Max OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
r = requests.get('http://www.ivsky.com/tupian/huwai_gongyuan_v50710/', headers=headers) #需下载图片的链接
#使用lxml解析网页
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src') #先找到所有的img
i = 0
path = 'D:\Python_Test/test_picture/' #指定下载文件路径
for img_url in img_urls:
    urllib.request.urlretrieve(img_url, path + 'img%s.jpg' % i, Schedule)
    i += 1
