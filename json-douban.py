import json
import requests

class Douban(object):
    def __init__(self):
        self.start_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"
        
        # 存放所有電影的 url
        self.url = []
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }

        for i in range(16):
            url = self.start_url.format(i*20)
            self.url.append(url)
        print (self.url)

        with open('douban.csv', 'a') as f:
            f.write('電影名稱, 評分, url, 圖片地址' + '\n')

    def get_json(self, url):
        result = requests.get(url, headers=self.headers)
        jsonDict = json.loads(result.text)
        content_list = []  # [{},{},{},{},{}]
        
        for i in jsonDict['subjects']:
            content = {} # 創建一個 dictionary
            
            content['電影名稱'] = i['title']
            content['評分'] = i['rate']
            content['url'] = i['url']
            content['img'] = i['cover']
            
            content_list.append(content)
        
        print(content_list)
        
        return content_list
    
    def save(self, content_list):
        # pass  # Suppose you are designing a new class with some methods that you don't want to implement, yet.
        with open('douban.csv', 'a') as f:
            for content in content_list:
                f.write(content['電影名稱'] + ',' + 
                        content['評分'] + ',' + 
                        content['url'] + ',' + 
                        content['img'] + '\n')
        
        
    
    def run(self):
        for url in self.url :
            content_list = self.get_json(url)
            self.save(content_list)
    
    
    
    
    
if __name__ == '__main__':
    douban = Douban()
    douban.run()


