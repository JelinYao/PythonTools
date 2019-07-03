# PythonTools
Python代码学习笔记，包括抓包、·WorldCloud、人脸识别等小功能


WorldCloud生词辛弃疾词云


    安装依赖库：使用pip3 install命令安装词云相关库（jieba、wordcloud），安装HTML爬虫工具（BeautifulSoup）
    代码逻辑：
    
    （1）请求辛弃疾词作页面
     页面URL：https://so.gushiwen.org/search.aspx ，通过参数page字段来请求不同的页面
     field = {
            "type":"author",
            "page":str(page_id),
            "value":"%E8%BE%9B%E5%BC%83%E7%96%BE",
        }
        
        
    （2）解析出页面中的词
     通过div查找到所有的词集：items = soup.find_all("div", {"class":"sons"})
     遍历其中的每一首词，获取词名、作者、内容：item_text = item_cont.find("div", {"class":"contson"})


     
     
    （3）词库解析，生成词云
      上面的遍历过程会把每一首词的内容分词后累加到一个字符串中：text = item_text.get_text()
      生成分词的词云图片，保存到本地后打开： 
        #打开词云图
        wc.generate(text)
        wc.to_file(img_path)
        os.startfile(img_path)
      
     ![辛弃疾词云](https://raw.githubusercontent.com/JelinYao/PythonTools/master/Xinqiji.png)
