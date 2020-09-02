# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 06-获取文本.py
@function:
@modify:
"""
from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

res = html.xpath('//a/text()')
print(res)  # ['first item', 'second item', 'third item', 'fourth item', 'fifth item']

res = html.xpath('//a[@href="link5.html"]/text()')
print(res)  # ['fifth item']

res = html.xpath('//li[@class="item-0"]/a/text()')
print(res)  # ['first item', 'fifth item']


