# coding:utf-8
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer

class SpiderMain(object):
    #初始化4个对象
    def __init__(self):
        self.urls=url_manager.UrlManager()#管理器
        self.downloader=html_downloader.HtmlDowanloader()#下载器
        self.parser=html_parser.HtmlParser()#解析器
        self.outputer=html_outputer.HtmlOutputer()#输出
    #调度程序 
    def craw(self,root_url):
        count =1 #初始化爬取得数目
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():#当有新的待爬取得url
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)#启动下载器 存储在cont
                new_urls,new_data=self.parser.parse(new_url,html_cont)#得到新的列表和数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)#收集数据
                if count==20:
                    break
                count = count+1
            except:
                print "爬取失败"
        self.outputer.output_html()
if __name__=="__main__":
    root_url="http://baike.baidu.com/item/%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%95%8C%E9%9D%A2"  #入口爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) #启动爬虫
    
