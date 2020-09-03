# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 01-简单使用.py
@function:
@modify:
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>hello world</p>', 'lxml')
print(soup.p.string)
