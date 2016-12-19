#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests

proxies = {
  'http' : 'socks5://127.0.0.1:1080',
  'https': 'socks5://127.0.0.1:1080'
}

r = requests.get("https://www.javbus.info",headers={'Connection':'close'},proxies = proxies)

print r.text
