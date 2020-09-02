# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 08-匹配所属性值.py
@function:
@modify:
"""

from lxml import etree

text = '''
<li class="li list"><a href="link1.html">item</a></li>
'''

html = etree.HTML(text)
res = html.xpath('//li[@class="li"]')
print(res)  # []

res = html.xpath('//li[contains(@class, "li")]')
print(res)  # [<Element li at 0x250269c5448>]
