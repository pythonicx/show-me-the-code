#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
0008:一个HTML文件，找出里面的正文。
0009:一个HTML文件，找出里面的链接。
'''


import re
import requests
from bs4 import BeautifulSoup


def get_html_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    reg = re.compile("<[^>]*>")
    content = reg.sub('', soup.prettify())
    return content


def get_html_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('a')

if __name__ == "__main__":
    url = 'http://www.baidu.com'
    req = requests.get(url)
    print(get_html_content(req.content))
    print(get_html_link(req.content))