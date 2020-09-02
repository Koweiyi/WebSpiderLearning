# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 03-获取子节点.py
@function:
@modify:
"""

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

# 通过 / 查找元素的直接子节点
res = html.xpath('//li/a')
print(res)
# output:[<Element a at 0x20a88593688>, <Element a at 0x20a885936c8>, <Element a at 0x20a88593708>, \
# <Element a at 0x20a88593748>, <Element a at 0x20a88593948>]

# 通过 // 查找元素的子孙节点
res = html.xpath('//ul//a')
# output:同上

res = html.xpath('//ul/a')
print(res)
# output: []
