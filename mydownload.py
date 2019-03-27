#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import requests
import datetime 

def Craw(url):
    html = requests.get(url).text
    urlPat = '<a href="(.*?)">.*?</a>'
    url = re.compile(urlPat).findall(html)
    print(url)
    namePat = '<a href=".*?">(.*?)</a>' 
    imgName = re.compile(namePat).findall(html)
    print(imgName)

def download(url):
    r = requests.get(url)
    img = r.content
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    imgName = nowTime + '.bmp'
    with open('./img/{}'.format(imgName), 'wb') as f:
        f.write(img)
    f.close()
    return './img/' + imgName 

if __name__ == '__main__':
    url = 'http://img.hcfyww.net/1d1484b4-3322-4883-915f-c3ba25775102.bmp'
    #Craw(url)
    download(url)

