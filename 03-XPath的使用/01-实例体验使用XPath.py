# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/02
@file: 01-实例体验使用XPath.py
@function:
@modify:
"""

from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)
res = etree.tostring(html)
print(res.decode('utf-8'))
'''
output:
<html><body><div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </li></ul>
</div>
</body></html>
添加了html和body标签并为我们补全了li标签
'''

# 也可以对文件进行解析
html = etree.parse('./test.html', etree.HTMLParser())
res = etree.tostring(html)
print(html)
print(type(html))
print(res.decode('utf-8'))

res = html.xpath('//*')
print(res)
print(type(res))
