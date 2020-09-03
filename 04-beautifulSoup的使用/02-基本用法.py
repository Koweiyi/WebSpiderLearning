# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 02-基本用法.py
@function:
@modify:
"""
from bs4 import BeautifulSoup

text = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
    <a href="http://example.com/lacie" class="sister" id="link2"></a>
    <a href="http://example.com/tillie" class="sister" id="link3"></a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
'''

soup = BeautifulSoup(text, 'lxml')
print(soup.prettify())
print(soup.title.string)
