#coding=utf-8
import requests
import re
import sys
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
print sys.getdefaultencoding()
reload(sys)
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()

class spider(object) :

    def changepage(self, url, total_page) :
        page_group = []
        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
        for i in range(now_page, total_page + 1) :
            link = re.sub('pageNum=\d+', 'pageNum=%s'%i, url, re.S) #部分替换
            page_group.append(link)
        return page_group

    def getsource(self, url) :
        html = requests.get(url)
        return html.text

    def geteveryclass(self, source) :
        everyclass = re.findall('(<li id=.*?</li>)', source, re.S)
        return everyclass

    def getinfo(self, eachclass) :
        info = {} #字典
        info['title'] = re.search('title="(.*?)" alt', eachclass, re.S).group(1)
        return info

    def saveinfo(self, classinfo) :
        f = open('info', 'w')
        for each in classinfo :
            f.writelines('title: ' + each['title'] + '\n')
        f.close()
        

if __name__ == '__main__' :
    classinfo = [] #列表
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider() #创建一个spider对象
    all_links = jikespider.changepage(url, 1) #获取所有链接
    for link in all_links :
        print u'正在处理页面： ' + link
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass :
            info = jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)
    

