#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
from Movie import movie
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")

proxies = {
  'http' : 'socks5://127.0.0.1:1080',
  'https': 'socks5://127.0.0.1:1080'
}

class download_state(object):
    error = 1
    downloading = 2
    success = 3
    failed = 4

def analyze_list_path(callback, path=""):
    "Analyze Movie On Url Path"
    if (not isinstance(path, str)) or len(path) == 0:
        callback(download_state.failed)
        return
    
    response = None
    try:
        response = requests.get(path.encode("utf8"), proxies=proxies)
    except expression as identifier:
        callback(download_state.error)
        return
    tree = etree.HTML(response.text.encode("utf8"))
    items = tree.xpath("//div[@class=\"item\"]")
    movies = []
    for item in items:
        a_movie = movie()
        href_node = item.xpath("a")
        if not isinstance(href_node, list) or len(href_node) == 0:
            continue
        href = href_node[0].get("href")
        image_node = item.xpath("a//img")
        if not isinstance(image_node, list) or len(image_node) == 0:
            continue
        image_url = image_node[0].get("src")
        title_node = item.xpath("a//span")
        if not isinstance(title_node, list) or len(title_node) == 0:
            continue
        title = title_node[0].text
        movie_number_node = item.xpath("a//date")
        if not isinstance(movie_number_node, list) or len(movie_number_node) == 0:
            continue
        movie_number = movie_number_node[0].text
        a_movie.movie_id = movie_number
        a_movie.title = title
        a_movie.cover_photo = image_url
        movies.append(a_movie)
    callback(download_state.success, movies)
    return
   

