#coding:utf-8
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print '获取所有的链接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()


print '获取lacie这个链接'
link_node = soup.find('a',class_='mnav', href='https://www.baidu.com')

print link_node

print '获取p段落名称'
link_node2 = soup.find('p',class_='title')
print link_node2