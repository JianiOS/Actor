#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
from bs4 import BeautifulSoup

proxies = {
  'http' : 'socks5://127.0.0.1:1080',
  'https': 'socks5://127.0.0.1:1080'
}

headers = {
    'User-Agent	' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 
}

html = requests.get("https://www.javbus.info/WANZ-101",headers={'Connection':'close'},proxies = proxies)

soup = BeautifulSoup(html.text.encode("utf-8"), "html.parser")

ajax_get_cili_url = 'https://www.javbus.info/ajax/uncledatoolsbyajax.php?lang=zh'
ajax_data = soup.select('script')[8].text
for l in ajax_data.split(';')[:-1]:
      ajax_get_cili_url += '&%s' % l[7:].replace("'","").replace(' ','')

print ajax_get_cili_url

def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    if Referer_url:
        headers['Referer'] = Referer_url
    req = requests.get(url, proxies=proxies, headers=headers)
    return req.content

b = get_html(ajax_get_cili_url,"https://www.javbus.info/WANZ-101")

print b
