#coding:utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
from setuptools.ssl_support import opener_for
from test.test_bs4 import soup
import urllib

url ="http://trains.ctrip.com/TrainBooking/RoundTrip.aspx?from=chongqing&to=nanjing&dayreturn=22&day=3&number=&fromCn=%D6%D8%C7%EC&toCn=%C4%CF%BE%A9"

print '第一种方法'
response1  = urllib2.urlopen(url)
soup = BeautifulSoup(response1,'html.parser',from_encoding='utf-8')
params = urllib.urlencode([('input_text', '重庆'), ('input_text', '南京')])
ink=soup.find('th')
print ink
print response1.getcode()
print len(response1.read())


