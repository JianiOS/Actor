#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from lxml import etree

reload(sys)
sys.setdefaultencoding("utf-8")

f = open("index.html", "r")
content = f.read()
f.close()

tree = etree.HTML(content.decode("utf-8"))


hrefs = tree.xpath("//div[@class='item']")
for href in hrefs:
    image = href.xpath("a//img")
    for img in image:
        print img.get("src")
        print img.get("title")

