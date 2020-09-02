# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 07-属性获取.py
@function:
@modify:
"""

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

res = html.xpath('//li[@class="item-inactive"]/a/@href')
print(res)  # ['link3.html']
