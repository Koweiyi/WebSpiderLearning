# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 11-节点轴选取.py
@function:
@modify:
"""
from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())

# 选择元素的直接父节点
res = html.xpath('//li[1]/parent::*')
print(res)  # [<Element ul at 0x25afd9a3788>]

# 选择元素的所有祖先节点
res = html.xpath('//li[1]/ancestor::*')
print(res)
# [<Element html at 0x210147c1e08>, <Element body at 0x21014923588>, \
# <Element div at 0x21014923608>, <Element ul at 0x210149237c8>]

# 选择元素的祖先节点中的div节点
res = html.xpath('//li[1]/ancestor::div')
print(res)  # [<Element div at 0x235f79d4688>]

# 选择元素属性
res = html.xpath('//li[1]/attribute::class')
print(res)  # ['item-0']

# 选择元素直接子节点相当于/
res = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(res)  # [<Element a at 0x24215ff6688>]

# 选择元素的子孙节点，相当于//
res = html.xpath('//ul/descendant::a[@href="link3.html"]/text()')
print(res)  # ['third item']

# 选择相邻节点
res = html.xpath('//li[3]/following-sibling::*/a/text()')
print(res)  # ['fourth item', 'fifth item']
