#coding=utf-8
'''
Created on 2013-1-28

@author: bjhbliu
'''
import urllib2

'''
content = urllib2.urlopen('http://XXXX').read()
'''
#headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"}
req = urllib2.Request('http://www.yi-see.com/read_141981_8965.html', headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"})
webpage = urllib2.urlopen(req)
content = webpage.read()
webpage.close()
#type = sys.getfilesystemencoding()#当前系统编码
#html = html.decode('GB2312').encode(type)#将网页转化成当前系统编码
#html = unicode(content, "gb2312").encode("utf8")
html = content.decode('GBK').encode('utf8')
print html

