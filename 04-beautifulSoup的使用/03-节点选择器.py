# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 03-节点选择器.py
@function:
@modify:
"""


from bs4 import BeautifulSoup
'''
直接调用节点的名称就可以选择节点元素，
再调用string就可以得到节点内的文本了
'''
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"></p>
<p class="story">once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
    <a href="http://example.com/lacie" class="sister" id="link2"></a>
    <a href="http://example.com/tillie" class="sister" id="link3"></a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.title)  # <title>The Dormouse's story</title>
print(type(soup.title))  # <class 'bs4.element.Tag'>
print(soup.title.string)  # The Dormouse's story
print(soup.head)  # <head><title>The Dormouse's story</title></head>
print(soup.p)  # <p class="title" name="dormouse"></p>
