import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers = headers)
html.encoding = 'utf-8'
#print html.text
title = re.findall('<span style="color:#666666;">(.*?)</span>', html.text, re.S)
for each in title :
    print each

chinese = re.findall('color: #039;">(.*?)</a>', html.text, re.S)
for each in chinese :
    print each
