#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

import os
import requests
from bs4 import BeautifulSoup


def get_imgurl(url):
    result = []
    req = requests.get(url)
    req.encoding = 'utf-8'
    bs = BeautifulSoup(req.content, 'html.parser')
    imgs = bs.find_all('img', 'BDE_Image')
    for img in imgs:
        result.append(img.get('src'))
    return result


def down_img(urls, dst_dir=os.getcwd()+'\\'+'CrawlerImg'):
    for url in urls:
        img = requests.get(url, stream=True)
        file_name = url.split("/")[-1]
        path = dst_dir + '\\' + file_name
        print('download img:',file_name)
        with open(path, 'wb') as f:
            for chunk in img.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            f.close()


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    img_src = get_imgurl(url)
    down_img(img_src)
    print('download has finished.')
