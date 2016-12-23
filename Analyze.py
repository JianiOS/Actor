#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
from Movie import movie
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")

proxies = {'http':'socks5://127.0.0.1:1080', 'https':'socks5://127.0.0.1:1080'}

class download_state(object):
    not_begin = 0
    error = 1
    downloading = 2
    success = 3
    failed = 4

def magnet_list_url(gid="", img="", uc=""):
    "Get Magnet list Url"
    url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?"
    if len(gid) > 0:
        url += "&gid=" + gid
    if len(img) > 0:
        url += "&img=" + img
    if len(uc) > 0:
        url += "&uc=" + uc
    return url

def analyze_magnet(html=""):
    "Analyze Magnet List"
    tree = None
    urls = []
    try:
        tree = etree.HTML(html.encode("utf8")).xpath("//tr")
    except Exception:
        pass
    if not isinstance(tree, list):
        return []
    if isinstance(tree, list) and len(tree) > 0:
        for tr_node in tree:
            a_node = tr_node.xpath("td/a")
            if isinstance(a_node, list) and len(a_node) > 0:
                magnet_url = a_node[0].get("href")
                urls.append(magnet_url)
                # urls.append(a_node[0].get("href").replace("'", ""))
    print urls
    return urls

def analyze_list_path(callback, path=""):
    "Analyze Movie On Url Path"
    if (not isinstance(path, str)) or len(path) == 0:
        callback(download_state.failed)
        return

    response = None
    try:
        response = requests.get(path.encode("utf8"), proxies=proxies)
    except:
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

        def detail_callback(download_state,download_urls=[], actors=[]):
            "Detail Call Back"
            pass
        analyze_detail_path(detail_callback, path=href)

    callback(download_state.success, movies)
    return

def analyze_detail_path(callback, path=""):
    "Analyze Movie Detail On Url Path"
    if (not isinstance(path, str)) or len(path) == 0:
        callback(download_state.error)
        return
    headers = {"Referer":path}
    response = None
    try:
        response = requests.get(path.encode("utf8"), proxies=proxies)
    except:
        callback(download_state.error)
        return
    content = response.text.encode("utf8")
    soup = BeautifulSoup(content, "html.parser")
    ajax_data = soup.select('script')[8].text
    params = ajax_data.split(";")
    param_dict = {}
    for var in params:
        var = var.replace("var", "").replace("\r", "").replace("\n", "").replace(" ", "").strip()
        single_para_array = var.split("=")
        if isinstance(single_para_array, list) and len(single_para_array) == 2:
            param_dict["{}".format(single_para_array[0])] = "{}".format(single_para_array[1])
    magnet_list_request_url = magnet_list_url(gid=param_dict["gid"], img=param_dict["img"], uc=param_dict["uc"])
    magnet_response = requests.get(magnet_list_request_url.encode("utf8"), proxies=proxies, headers=headers)
    urls = analyze_magnet(magnet_response.text)
    callback(download_state.error, download_urls=urls)


