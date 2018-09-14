import requests
from lxml import etree
import json

# 获取网页
def getOnePage(url,header):
    r = requests.get(url,headers=header)
    return r.text

# 解析网页
def parseOnePage(text):
    html = etree.HTML(text)
    names = html.xpath('//p[@class="name"]/a/@title')
    stars = html.xpath('//p[@class="star"]/text()')
    for index in range(len(names)):
        yield {
            '电影名':names[index],
            '主演':stars[index].strip()
        }

for offset in range(0,10):
    url = F'https://maoyan.com/board/4?offset={offset * 10}'
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    text = getOnePage(url,header)
    data = parseOnePage(text)
    for i in data:
        with open('./爬虫/猫眼TOP100电影/movies.txt','a',encoding='utf-8') as f:
            # 将字典转换成字符串
            dd = json.dumps(i,ensure_ascii=False) + '\n'
            f.write(dd)
