#coding=utf-8
# -*- coding:utf-8 -*-  
'''
Created on 2013-1-28

@author: bjhbliu
'''
import urllib2
#import sys
import re
from BeautifulSoup import BeautifulSoup
#import BeautifulSoup

'''
content = urllib2.urlopen('http://XXXX').read()
'''
#headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"}
req = urllib2.Request('http://www.yi-see.com/art_8965_6578.html', headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"})
webpage = urllib2.urlopen(req)
content = webpage.read()
webpage.close()

#type = sys.getfilesystemencoding()#当前系统编码
#html = html.decode('GB2312').encode(type)#将网页转化成当前系统编码
#html = unicode(content, "gb2312").encode("utf8")
html = content.decode('GBK').encode('utf8')
#print html

soup = BeautifulSoup(html)
#soup = BeautifulSoup(''.join(content))
#title = soup.find('title') #注意：返回的是list对象 
#print(title[0].contents)
print soup.title.string

#sections = soup.findAll(text=re.compile("第[0-9]{1}节"))
#sections = soup.findAll(text=re.compile("第\d{1,2}节"))
sections = soup.findAll('a', href=re.compile("read_\d{6}_\d{4}\.html"))
for item in sections:
    print item['href']
    chapterUrl = 'http://www.yi-see.com/' + item['href']
    print chapterUrl
    chapterReq = urllib2.Request(chapterUrl, headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0",'Host':'www.yi-see.com'})
    chapterPage = urllib2.urlopen(chapterReq)
    chapterContent = chapterPage.read()
    chapterPage.close()
    
    chapterHtml = chapterContent.decode('GBK').encode('utf8')
    #print chapterHtml    
    chapterSoup = BeautifulSoup(chapterHtml) 
    note = chapterSoup.find("td", {"class":"ART"})
#    print note.contents 
#    print note.text 

    fname = 'Z:/LiKuiNote.txt'
#   fname = unicode( 'Z:/李逵日记.txt', "utf8" ) 
    fsock = file(fname, 'a')
#    fname = 'Z:/李逵日记.txt'
#    fsock = open(fname, 'a')
    fsock.write(note.text)
    fsock.close()
#    break
#print sections[0]
