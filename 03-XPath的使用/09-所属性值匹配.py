# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 09-所属性值匹配.py
@function:
@modify:
"""
from lxml import etree

text = '''
<li class="li list" name="list"><a href="link.html">item</a></li>
'''

html = etree.HTML(text)

res = html.xpath('//li[contains(@class, "li") and @name="list"]/a/text()')
print(res)  # ['item']
