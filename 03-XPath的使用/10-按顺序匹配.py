# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 10-按顺序匹配.py
@function:
@modify:
"""
from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

res = html.xpath('//li[1]/a/text()')
print(res)  # ['first item']

res = html.xpath('//li[last()]/a/text()')
print(res)  # ['fifth item']

res = html.xpath('//li[position() < 3]/a/text()')
print(res)  # ['first item', 'second item']


