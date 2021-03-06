import requests
from Settings import HEADERS
import json
from ProxyPool.proxy_crawl import crawl_freeproxy
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

# Csdn_api,已经爬取了198篇文章

def get_urls():
    url_list = []
    category_list = ['Python', 'JAVA', 'web', 'arch', 'db', 'iot', 'fund']  # 七个模块
    for category in category_list:
        for page in range(6):
            csdn_api = f"https://blog.csdn.net/api/articles?type=more&category=python&shown_offset={page}"
            response = requests.get(csdn_api, headers=HEADERS)
            html = response.text
            data_json = json.loads(html)
            for article in data_json['articles']:
                url_list.append(article['url'])
    return url_list

def parse_urls(url_list: list):
    j = 0
    for i in range(len(url_list)):
        try:
            extractor = Extractor(threshold=30)
            html = extractor.getHtml(url_list[i])
            content = extractor.filter_tags(html)
            data = clean_content(extractor.getText(content))
            if data != "This   page   has   no   content   to   extract ":
                j += 1
                with open(f'E:/c++/毕业设计开发日志/06.文本数据集/数据清洗模块测试.txt', 'w+', encoding='utf-8') as txtfile:
                    txtfile.write(data)
                print(f"第{i+1}篇文章处理完毕")
            else:
                pass
        except Exception as e:
            print(e)

    print(f"共获取到{i}篇文章")
    print(f"成功处理{j}篇文章")


if __name__ == '__main__':
    url_list = get_urls()
    parse_urls(url_list)