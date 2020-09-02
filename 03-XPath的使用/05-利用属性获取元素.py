# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 05-利用属性获取元素.py
@function:
@modify:
"""
from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())

res = html.xpath('//li[@class="item-1"]')
print(len(res))
print(res)


