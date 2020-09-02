# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 04-获取父节点.py
@function:
@modify:
"""

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())

res = ' '.join(html.xpath('//a[@href="link3.html"]/../@id'))
print(res)

