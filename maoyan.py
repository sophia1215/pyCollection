import json
# http
import requests
from lxml import etree #wh1

class MaoYan(object):
  '''下載貓眼電影 Top 100'''
  
  # 初始化方法(函數)
  def __init__(self):
    # 應對-反爬措施
    # 當你訪問網址時，告訴服務器你是瀏覽器在訪問的。
    self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

  def getOnePage(self, url):
    '''獲取網頁源碼'''  
    html = requests.get(url, headers=self.header)
    return html.text

  def parseOnePage(self, text):
    '''
    解析網站，提取網站信息，用XPath
    '''
    html = etree.HTML(text)
    #電影名稱
    name = html.xpath('//p[@class="name"]//text()')
    #電影主演
    star = html.xpath('//p[@class="star"]//text()')
    
    # print(name)
    # print(star)

    for item in range(len(name)):
      yield {
        'name':name[item],
        'star':star[item].strip()
      }
  @staticmethod
  def write2File(content):
    '''寫入文件'''
    with open(r'maoyanTxt.txt', 'a', encoding='utf-8') as fp:
      fp.write(json.dumps(content, ensure_ascii=False) + '\n')

 
# 顯性調用
# MaoYan.getOnePage(MaoYan())

# 隱性調用
# maoyan = MaoYan()
# maoyan.getOnePage()

maoyan = MaoYan()
# 實參
# urls = 'http://maoyan.com/board/4'
urls = 'http://maoyan.com/board/4?offset=10'
html = maoyan.getOnePage(urls)
# print(html)
# 生成器 可迭代
text = maoyan.parseOnePage(html)

for item in text:
  maoyan.write2File(item)
  print(item)


