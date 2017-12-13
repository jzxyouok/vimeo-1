#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
proxies = {
    "http":"http://182.37.55.0:808",
    "http":"http://114.246.175.186:8118",
    "http":"http://112.114.93.107:8118",
    "http":"http://171.35.103.37:808",
    "http":"http://112.114.96.84:8118",
    "http":"http://112.114.94.162:8118",
    "http":"http://122.114.31.177:808",
    "http":"http://61.135.217.7:80",
    "http":"http://123.13.40.104:9999",
    "http":"http://123.56.169.22:3128",
    "http":"http://117.24.38.162:808",
}
def mv_id():
    url = 'https://vimeo.com/channels/staffpicks'
    html = requests.get(url,headers=headers,proxies=proxies).text
    ids = re.findall('"clip_id":(.*?),"is_staffpick":true,',html)
    for id in ids:
        urls = 'https://player.vimeo.com/video/'+str(id)+'?autoplay=1'
        html2 = requests.get(urls,headers=headers,proxies=proxies).text
        try:
            mv = re.findall('width":1920,"mime":"video/mp4","fps":.*?,"url":"(.*?)","cdn":"fastly","quality":"1080p"',html2)
            print(mv[0])
            with open('mvurl.txt','a') as f:
                f.write(mv[0]+'\n')
        except:
            pass
if __name__ == '__main__':
    mv_id()
