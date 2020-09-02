# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 02-获取所有li节点.py
@function:
@modify:
"""
from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

lis = html.xpath('//li')

for li in lis:
    print(li)
