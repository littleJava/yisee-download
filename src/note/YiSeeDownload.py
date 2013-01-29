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

#provice=raw_input('输入省名(请使用拼音):')
#city=raw_input("输入市名(请使用拼音):")
#url = "http://qq.ip138.com/weather/"+provice+"/"+city+".htm"
class YiSee():
    def __init__(self, url, filePath):
        self.url = url
        self.filePath = filePath
        pass
    
    def parseListContent(self):
        '''
        get the list contents,return the chapter collection
        '''
        listContent = self.getPageContent(self.url);
        sections = self.parseSections(listContent);
        return sections
    
    def getPageContent(self, url):
        '''
        content = urllib2.urlopen('http://XXXX').read()
        '''
        #headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"}
        req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/15.0"})
        webpage = urllib2.urlopen(req)
        content = webpage.read()
        webpage.close()
        
        #type = sys.getfilesystemencoding()#当前系统编码
        #html = html.decode('GB2312').encode(type)#将网页转化成当前系统编码
        #html = unicode(content, "gb2312").encode("utf8")
        html = content.decode('GBK').encode('utf8')
        #print html
        return html
    def parseSections(self, content):
        soup = BeautifulSoup(content)
        #soup = BeautifulSoup(''.join(content))
        #title = soup.find('title') #注意：返回的是list对象 
        #print(title[0].contents)
        print soup.title.string
        #sections = soup.findAll(text=re.compile("第[0-9]{1}节"))
        #sections = soup.findAll(text=re.compile("第\d{1,2}节"))
        sections = soup.findAll('a', href=re.compile("read_\d{6}_\d{4}\.html"))
        return sections
    '''
        parse the chapter collection,and write each chapter to the file
    '''
    def parseNoteContent(self, sections):
        for item in sections:
            print item['href']
            chapterUrl = 'http://www.yi-see.com/' + item['href']
            print chapterUrl
            chapterHtml = self.getPageContent(chapterUrl);
            #print chapterHtml    
            chapterSoup = BeautifulSoup(chapterHtml) 
            note = chapterSoup.find("td", {"class":"ART"})
            #print note.contents 
#            print note.text 
            self.writeFile(note.text, self.filePath);
            break
        #print sections[0]
        return
    def writeFile(self, content, filePath):
        #   fname = unicode( 'Z:/李逵日记.txt', "utf8" ) 
            fsock = file(filePath, 'a')
        #    fname = 'Z:/李逵日记.txt'
        #    fsock = open(fname, 'a')
            fsock.write(content)
            fsock.close()
            return
if __name__ == "__main__":
    download = YiSee("http://www.yi-see.com/art_8965_6578.html", unicode("Z:/李逵日记.txt",'utf8'))
    sections = download.parseListContent();
    download.parseNoteContent(sections);
    

