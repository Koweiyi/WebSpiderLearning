# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/04
@file: 01-txt文本存储.py
@function:
@modify:
"""
import requests

from lxml import etree
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

BASE_URL = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41'
    # 'User-Agent': UserAgent().random
}

resp = requests.get(BASE_URL, headers=headers).text
doc = pq(resp)

items = doc('.explore-tab .feed-item').items()
with open('zh_explore.txt', 'w', encoding='utf-8') as f:
    for item in items:
        question = item.find('h2').text()
        author = item.find('.author-link-line').text()
        answer = pq(item.find('.content').html()).text()
        f.write('\n'.join([question, author, answer]))
        f.write('\n' + '=' * 80 + '\n')
