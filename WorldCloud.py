#encodeing = utf-8
import os
import sys
import jieba
import wordcloud
import urllib
import urllib3
import certifi
import time
import html5lib
from bs4 import BeautifulSoup
import wordcloud
import jieba


def ParseWeb(url, page_id):
    try:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        }
        field = {
            "type":"author",
            "page":str(page_id),
            "value":"%E8%BE%9B%E5%BC%83%E7%96%BE",
        }
        r = http.request("GET", url, fields=field, headers=header)
        #print("r.data = %s"%r.data)
        #解析HTML
        soup = BeautifulSoup(r.data, "html5lib")
        items = soup.find_all("div", {"class":"sons"})
        out_text = ""
        for item in items:
            title = ""
            author = ""
            text = ""
            item_cont = item.find("div", {"class":"cont"})
            p = item_cont.find_all("p")
            for item_p in p:
                cls = item_p.get("class")
                if cls == None:#标题
                    a = item_p.find("b")
                    if a != None:
                        title = a.get_text()
                elif "source" in cls:#作者
                    a = item_p.find_all("a")[1]
                    span = a.find("span")
                    author = span.get_text()
            item_text = item_cont.find("div", {"class":"contson"})
            text = item_text.get_text()
            print("%s\r\n%s%s"%(title, author, text))
            out_text += JiebaParse(title+author+text)
    except Exception as e:
        print(e)
    finally:
        print("page id = %d"%page_id)
        return out_text


def JiebaParse(text):
    out_text = ""
    #分词
    for word in jieba.cut(text):
        if word.isspace() or word.isdigit():
                continue
        out_text += word + " "
    return out_text

if __name__ == '__main__':
    try:
        img_path = "C:\\Users\\yaojn\\Desktop\\backup\\code\\WordTest\\Xinqiji.png"
        font = 'C:\\Windows\\Fonts\\msyh.ttc'
        wc = wordcloud.WordCloud(font_path=font, #如果是中文必须要添加这个，否则会显示成框框
            background_color='black',
            width=1000,
            height=800,
        )
        url = "https://so.gushiwen.org/search.aspx"#https://so.gushiwen.org/search.aspx?type=author&page=9&value=%E8%BE%9B%E5%BC%83%E7%96%BE
        text = ""
        for i in range(1,21):
            text += ParseWeb(url, i)
            time.sleep(3)
        print("网页抓取完毕")
        #打开词云图
        wc.generate(text)
        wc.to_file(img_path)
        os.startfile(img_path)
    except Exception as e:
        print(e)
    finally:
        print("ok!")