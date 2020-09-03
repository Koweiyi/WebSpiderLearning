# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 读取html文件测试.py
@function:
@modify:
"""

with open('test.html', 'r', encoding='utf-8') as f:
    html = f.read()
    print(type(html))
